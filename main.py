import numpy as np
import pyaudio
import wave
import librosa
from mido import Message, MidiFile, MidiTrack

# parameters
format = pyaudio.paInt16
channels = 1
rate = 44100  # sample rate
chunk = 2048  # number of frames per buffer
record_seconds = 10
wave_output_file = "file.wav"

audio = pyaudio.PyAudio()

stream = audio.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

print("Recording...")

frames = []

# initialize MIDI output and add the track to it
midi_file = MidiFile()
track = MidiTrack()
midi_file.tracks.append(track)


# function to convert frequency to MIDI note
def freq_to_midi(freq):
    return int(librosa.hz_to_midi(freq))

try:
    for _ in range(0, int(rate / chunk * record_seconds)):
        try:
            audio_buffer = stream.read(chunk, exception_on_overflow=False)
            frames.append(audio_buffer)

            signal = np.frombuffer(audio_buffer, dtype=np.int16).astype(np.float32)

            # using librosa.pyin for pitch detection
            fmin = librosa.note_to_hz('C2')
            fmax = librosa.note_to_hz('C7')
            pitches, voiced_flags, _ = librosa.pyin(signal, fmin=fmin, fmax=fmax, sr=rate, frame_length=chunk)

            voiced_pitches = pitches[voiced_flags] # remove the unvoiced frames

            if len(voiced_pitches) > 0:
                pitch = np.median(voiced_pitches)
                midi_note = freq_to_midi(pitch)
                midi_msg = Message('note_on', note=midi_note, velocity=64, time=0)
                track.append(midi_msg)
                print("Pitch: {}, MIDI Note: {}".format(pitch, midi_note))

        except IOError as e:
            print(f"Error recording: {e}")

    print("Recording Finished...")

except KeyboardInterrupt:
    print("Recording Interrupted")
finally:
    if stream.is_active():
        stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(wave_output_file, 'wb')
    waveFile.setnchannels(channels)
    waveFile.setsampwidth(audio.get_sample_size(format))
    waveFile.setframerate(rate)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    midi_file.save('output.mid')
    print(f"Saved recording to {wave_output_file}")
    print("Saved MIDI to output.mid")
