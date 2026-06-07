import os
import sys
import wave
import subprocess
import tempfile

import numpy as np
import matplotlib

matplotlib.use("QtAgg", force=True)
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtWidgets import QFrame, QVBoxLayout, QWidget
from PySide6.QtCore import Signal, QTimer, Qt
from matplotlib.patches import Ellipse, Rectangle
import math

BG_COLOR = "#12131e"
NOTE_COLOR = "#00a7b0"
NOTE_EDGE_COLOR = "#00b5c9"

SOUNDFONT_PATH = os.path.join(os.path.dirname(__file__), "assets/Synth_Bamboo_Flute.sf2")


class MidiPlayback(QFrame):
    def __init__(self, midiframe, parent=None):
        super().__init__(parent)

        self.midiframe = midiframe

        self.fig = Figure(figsize=(10, 2), dpi=100)  # 10in2in would do
        self.ax = self.fig.add_subplot(111)
        self.fig.subplots_adjust(
            left=0.03,
            right=0.97,
            top=0.92,
            bottom=0.08,
        )

        self.ax.margins(x=0.02, y=0.35)
        self.ax.set_xlim(0, 100)  # will be updated based on MIDI length
        self.ax.set_ylim(0, 127)  # MIDI note range
        self.ax.axis("off")

        self.canvas = FigureCanvas(self.fig)
        self.layout = QVBoxLayout(self.midiframe)  # type: ignore
        self.layout.setContentsMargins(0, 0, 0, 0)  # type: ignore
        self.layout.addWidget(self.canvas)  # type: ignore

        self.fig.patch.set_facecolor(BG_COLOR)
        self.ax.set_facecolor(BG_COLOR)
        self.ax.axis("off")
        self.canvas.draw()

        self.loader_timer = QTimer(self)
        self.loader_timer.timeout.connect(self.update_loader)

        self.loader_frame = 0
        self.blobs = []

        self.notes = [
            (0.0, 1.0, 60),  # C4
            (0.5, 0.5, 64),  # E4
            (1.0, 1.0, 67),  # G4
        ]

        self.midi_length = 0.0

        self.midi_displayed = False

        self.playhead = None
        self.playhead_timer = QTimer(self)
        self.playhead_timer.timeout.connect(self._update_playhead)
        self.playhead_pos = 0.0
        self.playhead_speed = 1.0  # seconds of MIDI time per real second

    def load_midi(self, midi_file): 
        pass # TODO: will add later ;) for now just used set_notes with hardcoded notes for testing
    
    def stop_loader(self):
        self.loader_timer.stop()
        self.blobs.clear()

    def set_notes(self, notes):
        self.stop_loader()
        self.notes = notes

        self.ax.clear()
        self.ax.set_facecolor(BG_COLOR)
        self.ax.axis("off")

        for start, duration, note in self.notes:
            rect = Rectangle(
                (start, note - 0.45),
                max(duration, 0.03),
                0.9,
                facecolor=NOTE_COLOR,
                edgecolor=NOTE_EDGE_COLOR,
                linewidth=0.5,
            )
            self.ax.add_patch(rect)

        if self.notes:
            max_time = 0
            for note_data in self.notes:
                start = note_data[0]
                duration = note_data[1]
                end_time = start + duration
                if end_time > max_time:
                    max_time = end_time

            self.midi_length = max_time
            self.ax.set_xlim(0, max_time)

            pitches = [note[2] for note in self.notes]
            pitch_min = min(pitches)
            pitch_max = max(pitches)
            padding = 1

            self.ax.set_ylim(
                pitch_min - padding,
                pitch_max + padding,
            )

        self.canvas.draw()
        # mark that notes have been displayed
        self.midi_displayed = True

        # playhead init
        if self.playhead is not None:
            self.playhead.remove()

        self.playhead = self.ax.axvline(
            x=0,
            color="#737191",
            linewidth=1,
            alpha=0.6,
            visible=False,
        )

    def start_playhead(self):
        self.playhead.set_visible(True)
        self.playhead_timer.start(33)  # ~30fps

    def stop_playhead(self):
        self.playhead_timer.stop()
        self.canvas.draw_idle()

    def reset_playhead(self):
        self.stop_playhead()
        self.playhead_pos = 0.0
        if hasattr(self, 'playhead'):
            self.playhead.set_xdata([0, 0])
            self.playhead.set_visible(False)
            self.canvas.draw_idle()

    def show_loader(self):
        self.loader_timer.stop()
        self.ax.clear()
        self.ax.set_facecolor(BG_COLOR)

        self.ax.axis("off")

        self.canvas.draw()
        bbox = self.ax.get_window_extent()
        ax_width_px = bbox.width
        ax_height_px = bbox.height

        radius_in_axes_y = 0.08  # fraction of axes height
        radius_in_axes_x = radius_in_axes_y * (ax_height_px / ax_width_px) * 0.85 

        amplitude_y = radius_in_axes_y * 0.4
        amplitude_x = radius_in_axes_x * 0.4


        x_positions = [0.32, 0.46, 0.60, 0.74]  # x-positions of the 4 blobs (in axes coordinates, 0=left 1=right)
        y_center = 0.5

        self.blobs = []

        self._blob_base_w = radius_in_axes_x * 3
        self._blob_base_h = radius_in_axes_y * 2


        self._blob_amp_w = amplitude_x * 1.2
        self._blob_amp_h = amplitude_y * 1.2

        for x in x_positions:
            blob = Ellipse(
                (x, y_center),
                width=radius_in_axes_x * 2,
                height=radius_in_axes_y * 2,
                color=NOTE_COLOR,
                transform=self.ax.transAxes,
            )

            self.ax.add_patch(blob)
            self.blobs.append(blob)

        self.loader_frame = 0
        self.canvas.draw_idle()
        self.loader_timer.start(16)   # ~60fps

    def _update_playhead(self):
        self.playhead_pos += 0.033 * self.playhead_speed

        if self.playhead_pos >= self.midi_length:
            self.stop_playhead()
            return

        if self.playhead:
            self.playhead.set_xdata([self.playhead_pos, self.playhead_pos])

        self.canvas.draw_idle()

    def update_loader(self):
        self.loader_frame += 1
        t = self.loader_frame * 0.15

        for i, blob in enumerate(self.blobs):
            scale = math.sin(t + i * 0.8)
            blob.width = self._blob_base_w + self._blob_amp_w * scale
            blob.height = self._blob_base_h + self._blob_amp_h * scale
        self.canvas.draw_idle()

def render_midi_to_wav(midi_path, soundfont_path=SOUNDFONT_PATH, gain=3.0):
    """Render MIDI to a temp WAV file using fluidsynth. Returns the WAV path."""
    tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    tmp.close()
    try:
        subprocess.run([
            "fluidsynth",
            "-ni",
            "-g", str(gain),          # gain — default is 0.2, so 3.0 is much louder
            "-F", tmp.name,
            soundfont_path,
            midi_path,
        ], check=True)
    except subprocess.CalledProcessError as e:
        print("FluidSynth render failed:", e)
        return None

    return tmp.name


