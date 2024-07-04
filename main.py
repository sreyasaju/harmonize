import numpy as np
import pyaudio
import wave
import aubio

format = pyaudio.paInt16
channels = 1
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


tolerance = 0.9
fft_size = 4096
hop_size = chunk
pitch_o = aubio.pitch("default", fft_size, hop_size, rate)
pitch_o.set_unit("midi")
pitch_o.set_tolerance(tolerance)
print("Recording..")

frames = []


try:
    for _ in range(0, int(rate / chunk * record_seconds)):
        audio_buffer = stream.read(chunk)  # read no. of frames from audio stream
        frames.append(audio_buffer)

        signal = np.frombuffer(audio_buffer, dtype=np.float32)

        pitch = pitch_o(signal)[0]
        confidence = pitch_o.get_confidence()

        print("Pitch: {}, Confidence: {:.2f}".format(pitch, confidence))
    print("Recording Finished...")

except KeyboardInterrupt:
    print("Recording Interrupted")
finally:
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(wave_output_file, 'wb')
    waveFile.setnchannels(channels)
    waveFile.setsampwidth(audio.get_sample_size(format))
    waveFile.setframerate(rate)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    print(f"Saved recording to {wave_output_file}")