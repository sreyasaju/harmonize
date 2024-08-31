import pyaudio
import wave
import threading
import numpy as np
from PyQt6.QtWidgets import QFrame, QStatusBar
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
        self.xdata = np.arange(chunk)
        self.ydata = np.zeros(chunk)
        self.line, = self.ax.plot(self.xdata, self.ydata, lw=2, color='#45259b')

        self.ax.set_xlim(0, chunk)
        self.ax.set_ylim(-32768, 32767)

        self.fig.patch.set_facecolor('#12131e')
        self.ax.set_facecolor('#12131e')
        self.ax.axis('off')

        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.waveframe)
        self.canvas.setGeometry(self.waveframe.rect())
        self.canvas.draw()

    def start_recording(self, wave_output_file):
        if self.recording:
            return

        self.recording = True
        self.frames = []
        self.wave_output_file = wave_output_file

        self.record_thread = threading.Thread(target=self._record)
        self.record_thread.start()

    def _record(self):
        self.stream = self.audio.open(format=format,
                                      channels=channels,
                                      rate=rate,
                                      input=True,
                                      frames_per_buffer=chunk)
        print("Recording started...")

        while self.recording:
            data = self.stream.read(chunk)
            self.frames.append(data)
            self._update_plot(data)

        self.stream.stop_stream()
        self.stream.close()

        # save the recorded audio to a file
        with wave.open(self.wave_output_file, 'wb') as waveFile:
            waveFile.setnchannels(channels)
            waveFile.setsampwidth(self.audio.get_sample_size(format))
            waveFile.setframerate(rate)
            waveFile.writeframes(b''.join(self.frames))

        print(f"Recording saved to {self.wave_output_file}")


    def stop_recording(self):
        if not self.recording:
            return
        self.recording = False

    def _update_plot(self, data):
        new_data = np.frombuffer(data, dtype=np.int16)

        self.ydata = np.roll(self.ydata, -len(new_data))
        self.ydata[-len(new_data):] = new_data

        self.line.set_ydata(self.ydata)
        self.canvas.draw()
        return self.line
