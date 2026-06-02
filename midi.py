import librosa
import numpy as np
from mido import Message, MidiFile, MidiTrack
import scipy.signal
from mido import MetaMessage


def freq_to_midi(freq):
    return int(round(librosa.hz_to_midi(freq)))

def midi_to_alphabet(midi_note):
    if 0 <= midi_note <= 127:
        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        
        # MIDI note 0 is C in octave -1 
        octave = midi_note // 12 - 1
        note = note_names[midi_note % 12]
        return f"{note}{octave}"
    

def convert_to_midi(wave_output_file, midi_output, silence_threshold=-40.0):
    # TEST: Use test_sample.wav for testing
    wave_output_file = "lily.wav"
    # wave_output_file = wave_output_file  # Original
    
    signal, sr = librosa.load(wave_output_file, sr=None)

    # Calculate the RMS energy of the signal
    rms = librosa.feature.rms(y=signal, frame_length=2048, hop_length=512)
    rms_db = librosa.amplitude_to_db(rms, ref=np.max)
    n_rms_frames = rms_db.shape[1]

    fmin = librosa.note_to_hz('C2')
    fmax = librosa.note_to_hz('C7')
    pitches, voiced_flags, _ = librosa.pyin(signal, fmin=fmin, fmax=fmax, sr=sr) #voiced_flags is boolean -> noise vs silence. _ is confidence level of the pitch estimation

    midi_file = MidiFile()
    track = MidiTrack()
    midi_file.tracks.append(track)

    hop_length = 512
    ticks_per_beat = midi_file.ticks_per_beat
    tempo = 500000  # default tempo (120 BPM), so 500000 microseconds per beat
    ticks_per_second = (ticks_per_beat * 1000000) / tempo 

    last_pitch = None
    last_time = 0


    stability_threshold = 3
    
    stable_pitch = None
    test_pitch = None
    test_count = 0
    
    track.append(MetaMessage('set_tempo', tempo=tempo, time=0))

    for i, (pitch, voiced_flag) in enumerate(zip(pitches, voiced_flags)):

        rms_index = min(i, n_rms_frames - 1)
        rms_value = rms_db[0][rms_index] # loudness of the current frame in dB,  [0] -> single row, [i] -> frame index
        current_time = int((i*hop_length) / sr * ticks_per_second)

        if voiced_flag and rms_value > silence_threshold:
            midi_note = freq_to_midi(pitch)

            if midi_note == test_pitch:
                test_count += 1
            else:
                test_pitch = midi_note
                test_count = 1

            # only act on a pitch once its stable for N consecutive frames to avoid rapid note changes due to pitch estimation noise
            if test_count >= stability_threshold:
                if stable_pitch is not None and stable_pitch != test_pitch:
                    duration = current_time - last_time

                    track.append(Message('note_off', note=stable_pitch, velocity=64, time=duration))

                    stable_pitch = None
                    last_time = current_time


                # note on for the current note
                if stable_pitch is None:
                    on_delta = current_time - last_time
                    track.append(Message('note_on', note=midi_note, velocity=64, time=on_delta))
                    stable_pitch = test_pitch
                    last_time = current_time

                    alphabet = midi_to_alphabet(midi_note)
                    if alphabet:
                        print(f"Pitch: {pitch:.2f}, MIDI Note: {alphabet}")
                    else:
                        print(f"No alphabet mapping found for MIDI Note {midi_note}")

        else:

            test_pitch = None
            test_count = 0

            piano_roll_notes = []

            if stable_pitch is not None:
                duration = current_time - last_time
                start_sec = last_time / ticks_per_second
                duration_sec = duration / ticks_per_second
                piano_roll_notes.append((start_sec,duration_sec,stable_pitch))
                track.append(Message('note_off', note=stable_pitch, velocity=64, time=duration))
                stable_pitch = None
                last_time = current_time


    # note off for the last note
    if stable_pitch is not None:
        end_time = int(len(signal) / sr * ticks_per_second)
        duration = max(0, end_time - last_time)
        start_sec = last_time / ticks_per_second
        duration_sec = duration / ticks_per_second
        piano_roll_notes.append((start_sec,duration_sec,stable_pitch))
        track.append(Message('note_off', note=stable_pitch, velocity=64, time=duration))

    # save the MIDI file
    midi_file.save(midi_output)
    return piano_roll_notes
    print(f"Saved MIDI to {midi_output}")
    