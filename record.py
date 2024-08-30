import pyaudio
import wave
import threading
import numpy as np
from PyQt6.QtWidgets import QFrame
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

format = pyaudio.paInt16
channels = 1
rate = 44100
chunk = 1024


class RecordAudio(QFrame):
    def __init__(self, waveframe, parent=None):
        super().__init__(parent)
        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.frames = []
        self.recording = False
        self.wave_output_file = None
        self.record_thread = None
        self.waveframe = waveframe

        self.fig = Figure(figsize=(10, 2), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.line, = self.ax.plot([], [], lw=1, color='#45259b')

        # Set background color and hide the axes
        self.fig.patch.set_facecolor('#12131e')
        self.ax.set_facecolor('#12131e')
        self.ax.spines['top'].set_color('none')
        self.ax.spines['right'].set_color('none')
        self.ax.spines['left'].set_color('none')
        self.ax.spines['bottom'].set_color('none')
        self.ax.xaxis.set_visible(False)
        self.ax.yaxis.set_visible(False)

        self.ax.set_ylim(-32768, 32767)
        self.ax.set_xlim(0, chunk)

        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.waveframe)
        self.canvas.setGeometry(self.waveframe.rect())
        self.canvas.draw()

    def start_recording(self, wave_output_file):
        """Start audio recording in a separate thread."""
        if self.recording:
            return

        self.recording = True
        self.frames = []
        self.wave_output_file = wave_output_file

        self.record_thread = threading.Thread(target=self._record)
        self.record_thread.start()

    def _record(self):
        """Internal method to handle the recording process."""
        self.stream = self.audio.open(format=format,
                                      channels=channels,
                                      rate=rate,
                                      input=True,
                                      frames_per_buffer=chunk)
        print("Recording started...")

        while self.recording:
            data = self.stream.read(chunk)
            self.frames.append(data)
            self._update_plot()

        self.stream.stop_stream()
        self.stream.close()

        with wave.open(self.wave_output_file, 'wb') as waveFile:
            waveFile.setnchannels(channels)
            waveFile.setsampwidth(self.audio.get_sample_size(format))
            waveFile.setframerate(rate)
            waveFile.writeframes(b''.join(self.frames))

        print(f"Recording saved to {self.wave_output_file}")

    def stop_recording(self):
        """Stop the audio recording."""
        if not self.recording:
            return
        self.recording = False

    def _update_plot(self, *args):
        if not self.frames:
            return

        data = np.frombuffer(self.frames[-1], dtype=np.int16)
        self.line.set_data(np.arange(len(data)), data)
        self.ax.set_ylim(np.min(data), np.max(data))
        self.canvas.draw()
        return self.line