import pyaudio
import subprocess
import wave

# parameters
format = pyaudio.paInt16
channels = 1
rate = 44100  # number of samples
chunk = 1024 #  number of frames in the buffer
record_seconds = 30
wave_output_file = "file.wav"

def record_audio():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)
    print("Recording..")
    frames = []

    try:
        for i in range(0, int(rate/chunk*record_seconds)):
            data = stream.read(chunk)  # read no. of frames from audio stream
            frames.append(data)
            # appends data to the frame list
        print("Recording Finished...")

    except KeyboardInterrupt:
        print("Recording interrupted...")

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

        print(f"Recording saved to {wave_output_file}")

        subprocess.run(["python3", "midi.py"])

if __name__ == "__main__":
    record_audio()