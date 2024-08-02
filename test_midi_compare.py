import pytest
def load_file(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f]

def test_pitch_debugging():
    """Test if the debugging the pitch matches the sample."""
    sample_pitches = load_file("sample_pitches.txt")
    debugged_pitches = load_file("debugged_pitches.txt")

    assert sample_pitches == debugged_pitches, "Pitch debugging output does not match!"

