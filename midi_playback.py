import os
import sys
import wave

import numpy as np
import matplotlib

matplotlib.use("QtAgg", force=True)
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtWidgets import QFrame, QVBoxLayout, QWidget
from PySide6.QtCore import Signal, QTimer, Qt
from matplotlib.patches import Circle, Rectangle
from matplotlib.animation import FuncAnimation
import math

BG_COLOR = "#12131e"
NOTE_COLOR = "#00a7b0"
NOTE_EDGE_COLOR = "#00b5c9"


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

        self.notes = [
            (0.0, 1.0, 60),  # C4
            (0.5, 0.5, 64),  # E4
            (1.0, 1.0, 67),  # G4
        ]

        self.midi_length = 0

        self.midi_displayed = False

    def load_midi(self, midi_file): 
        pass # TODO: will add later ;) for now just used set_notes with hardcoded notes for testing
    
    def stop_loader(self):
        if hasattr(self, '_loader_animation') and self._loader_animation is not None:
            self._loader_animation.event_source.stop()
            self._loader_animation = None

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

    def show_loader(self):
        self.ax.clear()
        self.ax.set_facecolor(BG_COLOR)

        self.ax.axis("off")

        x_positions = [0.2, 0.4, 0.6, 0.8]  # x-positions of the 4 blobs (in axes coordinates, 0=left 1=right)
        radius = 0.06
        amplitude = 0.04
        phase_step = 0.8 # offset between the blobs (radians)

        self.blobs = []

        for x in x_positions:
            circle = Circle((x, 0.5), radius, color=NOTE_COLOR, transform=self.ax.transAxes, clip_on=False)

            self.ax.add_patch(circle)
            self.blobs.append(circle)

        
        def animate(frame):
            t = frame * 0.045
            for i, blob in enumerate(self.blobs):
                r = radius + amplitude * math.sin(t + i * phase_step)
                blob.set_radius(r)
                blob.set_facecolor(NOTE_COLOR)
            return self.blobs
        
        self._loader_animation = FuncAnimation(self.fig, animate, frames=200, interval=50, blit=True, cache_frame_data=False)
        self.canvas.draw()
