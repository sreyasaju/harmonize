import pytest
import midi


def load_file(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f]


def test_pitch_debugging_matches_midi_module():
    """Generate note names using `midi` functions and compare to the sample output."""
    sample_lines = load_file("sample_pitches.txt")

    for line in sample_lines:
        # expected format: "Pitch: 266.20, MIDI Note: C4"
        if not line:
            continue
        pitch_part = line.split(",")[0].strip()
        pitch_value = float(pitch_part.split("Pitch:")[1])

        midi_note = midi.freq_to_midi(pitch_value)
        alphabet = midi.midi_to_alphabet(midi_note)

        generated = f"Pitch: {pitch_value:.2f}, MIDI Note: {alphabet}"
        assert generated == line, f"Mismatch: expected '{line}' got '{generated}'"

