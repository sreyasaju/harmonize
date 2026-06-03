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


            self.fig = Figure(figsize=(10, 2), dpi=100) #10in2in would do
            self.ax = self.fig.add_subplot(111)
            self.ax.set_xlim(0, 100) # will be updated based on MIDI length
            self.ax.set_ylim(0, 127) # MIDI note range
            self.ax.axis('off')

            self.canvas = FigureCanvas(self.fig)
            self.layout = QVBoxLayout(self.midiframe) # type: ignore
            self.layout.setContentsMargins(0, 0, 0, 0) # type: ignore
            self.layout.addWidget(self.canvas) # type: ignore

            self.fig.patch.set_facecolor('#12131e')
            self.ax.set_facecolor('#12131e')
            self.ax.axis('off')
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

            for start, duration, note in self.notes:
                rect = Rectangle(
                    (start, note - 0.4),  # x,y
                    duration,             # width
                    0.8                   # height
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

                pitches = []

                for note in self.notes:
                    pitches.append(note[2])

                self.ax.set_ylim(
                    min(pitches) - 2,
                    max(pitches) + 2
                )

                self.canvas.draw()

