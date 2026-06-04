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
from PySide6.QtCore import Signal

import sys

format = pyaudio.paInt16 # 16 bits per sample, standard
channels = 1 # mono
rate = 44100 #this is standard sample rate
chunk = 1024 # number of frames per buffer

class RecordAudio(QFrame):
    update_signal = Signal(float, float) #peak_min, peak_max

    def __init__(self, waveframe, parent=None):
        super().__init__(parent)
        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.frames = []
        self.recording = False
        self.wave_output_file = None
        self.record_thread = None

        self.canvas_width = 2000  # matches figsize(10) * dpi(100)

        self.write_head = 0
        self.peaks_min = np.zeros(self.canvas_width)
        self.peaks_max = np.zeros(self.canvas_width)        

        self.sample_peak = 0 # used for dynamic y-axis scaling based on audio peak values

        self.waveframe = waveframe
        self.fig = Figure(figsize=(10, 2), dpi=100) #10in2in would do
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim(0, self.canvas_width)
        self.ax.set_ylim(-32768, 32767)

        self.ax.margins(x=0.03, y=0.03)

        self.vlines = self.ax.vlines(
            np.arange(self.canvas_width),
            self.peaks_min,
            self.peaks_max,
            colors="#00b0a4"
            )

        self.update_signal.connect(self._update_plot)

        self.fig.patch.set_facecolor('#12131e')
        self.ax.set_facecolor('#12131e')
        self.ax.axis('off')

        self.canvas = FigureCanvas(self.fig)
        self.layout = QVBoxLayout(self.waveframe) # type: ignore
        self.layout.setContentsMargins(0, 0, 0, 0) # type: ignore
        self.layout.addWidget(self.canvas) # type: ignore
        self.canvas.draw()
        
        self.gain = 1.0
    def get_output_dir(self):
        if getattr(sys, 'frozen', False):
            # user's home directory to avoid permission issues
            return os.path.expanduser("~/Harmonize")
        else:
            # dev -> cwd ;)
            return os.getcwd()

    def start_recording(self, wave_output_file):

        self.write_head = 0
        self.peaks_min = np.zeros(self.canvas_width)
        self.peaks_max = np.zeros(self.canvas_width)
        self.sample_peak = 0  # reset the sameple peak for new recording,  so that the y-axis scaling can adjust to the new audio levels ;)

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
                data = self.stream.read(chunk, exception_on_overflow=False)

                raw_data = np.frombuffer(data, dtype=np.int16)

                if self.gain != 1.0:
                    scaled_data = np.clip(raw_data.astype(np.float32)* self.gain, -32768, 32767) #synatx (array,min,max)
                    scaled_data = scaled_data.astype(np.int16)
                else:
                    scaled_data = raw_data

                self.frames.append(scaled_data.tobytes())

                peak_max = int(scaled_data.max())
                peak_min = int(scaled_data.min())

                self.update_signal.emit(peak_min, peak_max)


        except Exception as e:
            print(f"Error during recording: {e}")

        finally:
            self.recording = False

            if self.stream is not None:
                self.stream.stop_stream()
                self.stream.close()

        # save the recorded audio to a file
        with wave.open(self.wave_output_file, 'wb') as waveFile: # type: ignore
            waveFile.setnchannels(channels)
            waveFile.setsampwidth(self.audio.get_sample_size(format))
            waveFile.setframerate(rate)
            waveFile.writeframes(b''.join(self.frames))

        print(f"Recording saved to {self.wave_output_file}")

    def update_gain(self, gain_value):
        self.gain = float(gain_value)

    def stop_recording(self):
        if not self.recording:
            return
        self.recording = False

        if self.record_thread is not None:
            self.record_thread.join()

    def _update_plot(self, peak_min, peak_max):

        threshold = 95
        if max(abs(peak_min), abs(peak_max)) < threshold:
            peak_min = -10
            peak_max = 10

        if self.write_head < self.canvas_width:
            self.peaks_min[self.write_head] = peak_min
            self.peaks_max[self.write_head] = peak_max
            self.write_head += 1
        else:
            self.peaks_min = np.roll(self.peaks_min, -1)
            self.peaks_max = np.roll(self.peaks_max, -1)
            self.peaks_min[-1] = peak_min
            self.peaks_max[-1] = peak_max

        segments = []
        for x in range(0, self.write_head):
            start_point = (x, self.peaks_min[x])
            end_point = (x, self.peaks_max[x])
            segments.append([start_point, end_point])
        
        current_peak = max(abs(peak_min), abs(peak_max))
        if current_peak > self.sample_peak:
            self.sample_peak = current_peak
            self.ax.set_ylim(-self.sample_peak, self.sample_peak)

        self.vlines.set_segments(segments)

        self.canvas.draw_idle() # redrawing...