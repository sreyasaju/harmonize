import os
import sys
import wave

import numpy as np
import matplotlib

matplotlib.use("QtAgg", force=True)
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtWidgets import QFrame, QVBoxLayout
from PySide6.QtCore import Signal
from matplotlib.patches import Rectangle


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

        self.fig.patch.set_facecolor("#12131e")
        self.ax.set_facecolor("#12131e")
        self.ax.axis("off")
        self.canvas.draw()

        self.notes = [
            (0.0, 1.0, 60),  # C4
            (0.5, 0.5, 64),  # E4
            (1.0, 1.0, 67),  # G4
        ]

        self.midi_length = 0

    def load_midi(self, midi_file): 
        pass # TODO: will add later ;) for now just used set_notes with hardcoded notes for testing

    def set_notes(self, notes):
        self.notes = notes

        self.ax.clear()
        self.ax.set_facecolor("#12131e")
        self.ax.axis("off")

        for start, duration, note in self.notes:
            rect = Rectangle(
                (start, note - 0.45),
                max(duration, 0.03),
                0.9,
                facecolor="#00b0a4",
                edgecolor="#00ffb3",
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


