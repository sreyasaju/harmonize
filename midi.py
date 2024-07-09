import numpy as np
import librosa
from mido import Message, MidiFile, MidiTrack


wave_output_file = "file.wav"
midi_output = "output.mid"

# function to convert frequency to MIDI note
def freq_to_midi(freq):
    return int(librosa.hz_to_midi(freq))

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
        81: 'A5', 82: 'A#5', 83: 'B5',84: 'C6', 85: 'C#6',
        86: 'D6', 87: 'D#6', 88: 'E6', 89: 'F6', 90: 'F#6',
        91: 'G6', 92: 'G#6', 93: 'A6', 94: 'A#6', 95: 'B6',
        96: 'C7'
    }

    if midi_note in note_mapping:
        return note_mapping[midi_note]
    else:
        return None


def convert_to_midi():
    signal, sr = librosa.load(wave_output_file, sr=None)

    # using librosa.pyin for pitch detection
    fmin = librosa.note_to_hz('C2')
    fmax = librosa.note_to_hz('C7')
    pitches, voiced_flags, _ = librosa.pyin(signal, fmin=fmin, fmax=fmax, sr=sr)

    # initialize MIDI output and add the track to it
    midi_file = MidiFile()
    track = MidiTrack()
    midi_file.tracks.append(track)

    time_counter = 0

    voiced_pitches = pitches[voiced_flags]  # remove the unvoiced frames
    for pitch in voiced_pitches:
        midi_note = freq_to_midi(pitch)
        midi_msg = Message('note_on', note=midi_note, velocity=64, time=time_counter)
        track.append(midi_msg)

        alphabet = midi_to_alphabet(midi_note)
        if alphabet:
            print(f"Pitch: {pitch:.2f}, MIDI Note: {alphabet}")
        else:
            print(f"No alphabet mapping found for MIDI Note {midi_note}")
        time_counter += 1

    # Save the MIDI file
    midi_file.save(midi_output)
    print(f"Saved MIDI to {midi_output}")


if __name__ == "__main__":
    convert_to_midi()
