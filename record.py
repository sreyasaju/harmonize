import pyaudio
import wave
import threading

format = pyaudio.paInt16
channels = 1
rate = 44100
chunk = 1024

class RecordAudio:
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.frames = []
        self.recording = False
        self.wave_output_file = None
        self.record_thread = None

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


        self.stream.stop_stream()
        self.stream.close()

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
        if self.record_thread:
            self.record_thread.join()
        print("Recording stopped...")