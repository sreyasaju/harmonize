import pyaudio
import wave

format = pyaudio.paInt16
channels = 2
rate = 44100  # number of samples
chunk = 1024 #  number of frames in the buffer
record_seconds = 5
wave_output_file = "file.wav"

audio = pyaudio.PyAudio()

stream = audio.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)
print("Recording..")

frames = []

for i in range(0, int(rate/chunk*record_seconds)):
    data = stream.read(chunk)  # read no. of frames from audio stream
    frames.append(data) # appends data to the frame list
print("Recording Finished...")
