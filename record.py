import pyaudio
import wave

# Define audio parameters
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

    def start_recording(self, wave_output_file):
        if self.recording:
            return  # recording

        self.recording = True
        self.frames = []
        self.wave_output_file = wave_output_file

        self.stream = self.audio.open(format=format,
                                      channels=channels,
                                      rate=rate,
                                      input=True,
                                      frames_per_buffer=chunk)
        print("Recording started...")

    def stop_recording(self):
        if not self.recording:
            return  # not recording

        self.recording = False
        print("Recording stopped...")

        self.stream.stop_stream()
        self.stream.close()

        with wave.open(self.wave_output_file, 'wb') as waveFile:
            waveFile.setnchannels(channels)
            waveFile.setsampwidth(self.audio.get_sample_size(format))
            waveFile.setframerate(rate)
            waveFile.writeframes(b''.join(self.frames))

        print(f"Recording saved to {self.wave_output_file}")

    def read_audio(self):
        if self.recording:
            data = self.stream.read(chunk)
            self.frames.append(data)