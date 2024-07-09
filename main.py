import numpy as np
import pyaudio
import wave
import librosa
from mido import Message, MidiFile, MidiTrack

# Parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100  # Sample rate
CHUNK = 1024  # Number of frames per buffer
RECORD_SECONDS = 60
WAVE_OUTPUT_FILE = "file.wav"

audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

print("Recording...")

frames = []

# Initialize MIDI output and add the track to it
midi_file = MidiFile()
track = MidiTrack()
midi_file.tracks.append(track)

# Function to convert frequency to MIDI note
def freq_to_midi(freq):
    return int(librosa.hz_to_midi(freq))

# Function to map MIDI note to alphabet
def midi_to_alphabet(midi_note):
    note_mapping = {
        36: 'C2', 37: 'C#2', 38: 'D2', 39: 'D#2', 40: 'E2',
        41: 'F2', 42: 'F#2', 43: 'G2', 44: 'G#2', 45: 'A2',
        46: 'A#2', 47: 'B2', 48: 'C3', 49: 'C#3', 50: 'D3',
        51: 'D#3', 52: 'E3', 53: 'F3', 54: 'F#3', 55: 'G3',
        56: 'G#3', 57: 'A3', 58: 'A#3', 59: 'B3', 60: 'C4',
        61: 'C#4', 62: 'D4', 63: 'D#4', 64: 'E4', 65: 'F4',
        66: 'F#4', 67: 'G4', 68: 'G#4', 69: 'A4', 70: 'A#4',
        71: 'B4', 72: 'C5', 73: 'C#5', 74: 'D5', 75: 'D#5',
        76: 'E5', 77: 'F5', 78: 'F#5', 79: 'G5', 80: 'G#5',
        81: 'A5', 82: 'A#5', 83: 'B5', 84: 'C6', 85: 'C#6',
        86: 'D6', 87: 'D#6', 88: 'E6', 89: 'F6', 90: 'F#6',
        91: 'G6', 92: 'G#6', 93: 'A6', 94: 'A#6', 95: 'B6',
        96: 'C7'
    }
    return note_mapping.get(midi_note, None)

try:
    time_counter = 0
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        try:
            audio_buffer = stream.read(CHUNK, exception_on_overflow=False)
            frames.append(audio_buffer)

            signal = np.frombuffer(audio_buffer, dtype=np.int16).astype(np.float32)

            # Using librosa.pyin for pitch detection
            fmin = librosa.note_to_hz('C2')
            fmax = librosa.note_to_hz('C7')
            pitches, voiced_flags, _ = librosa.pyin(signal, fmin=fmin, fmax=fmax, sr=RATE, frame_length=CHUNK)

            voiced_pitches = pitches[voiced_flags]  # Remove the unvoiced frames

            if len(voiced_pitches) > 0:
                pitch = np.median(voiced_pitches)
                midi_note = freq_to_midi(pitch)
                midi_msg = Message('note_on', note=midi_note, velocity=64, time=time_counter)
                track.append(midi_msg)

                alphabet = midi_to_alphabet(midi_note)
                if alphabet:
                    print("Pitch: {}, MIDI Note: {}".format(pitch, alphabet))
                else:
                    print(f"No alphabet mapping found for MIDI Note {midi_note}")
                time_counter += 1

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

    waveFile = wave.open(WAVE_OUTPUT_FILE, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    midi_file.save('output.mid')
    print(f"Saved recording to {WAVE_OUTPUT_FILE}")
    print("Saved MIDI to output.mid")
