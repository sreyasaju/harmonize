import os
os.environ.setdefault("QT_API", "pyside6")

import pyaudio
import wave
import threading
import numpy as np
import matplotlib
matplotlib.use("QtAgg", force=True)
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtWidgets import QFrame, QVBoxLayout
import sys

format = pyaudio.paInt16 # 16 bits per sample, standard
channels = 1 # mono
rate = 44100 #this is standard sample rate
chunk = 1024 # number of frames per buffer

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
        self.fig = Figure(figsize=(10, 2), dpi=100) #10in2in would do
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
        self.layout = QVBoxLayout(self.waveframe)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.canvas)
        self.canvas.draw()

    def get_output_dir(self):
        if getattr(sys, 'frozen', False):
            # user's home directory to avoid permission issues
            return os.path.expanduser("~/Harmonize")
        else:
            # dev -> cwd ;)
            return os.getcwd()

    def start_recording(self, wave_output_file):
        if self.recording:
            return
        self.recording = True
        self.frames = []
        output_dir = self.get_output_dir()
        self.wave_output_file = os.path.join(output_dir, wave_output_file)

        self.record_thread = threading.Thread(target=self._record)
        self.record_thread.start()

    def _record(self):
        try: 
            self.stream = self.audio.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)
            print("Recording started...")

            while self.recording:
                data = self.stream.read(chunk)
                self.frames.append(data)
                self._update_plot(data)

        except Exception as e:
            print(f"Error during recording: {e}")

        finally:
            self.recording = False
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

        if self.record_thread is not None:
            self.record_thread.join()

    def _update_plot(self, data):
        new_data = np.frombuffer(data, dtype=np.int16) #raw audio --> numpy array int16!

        self.ydata = np.roll(self.ydata, -len(new_data))
        self.ydata[-len(new_data):] = new_data

        self.line.set_ydata(self.ydata)
        self.canvas._draw_idle() # redrawing...
        return self.line
