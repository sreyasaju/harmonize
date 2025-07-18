import librosa
import numpy as np
from mido import Message, MidiFile, MidiTrack
import scipy.signal

def freq_to_midi(freq):
    return int(librosa.hz_to_midi(freq))

def midi_to_alphabet(midi_note):
    if 0 <= midi_note <= 127:
        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        
        # MIDI note 0 is C in octave -1 
        octave = midi_note // 12 - 1
        note = note_names[midi_note % 12]
        return f"{note}{octave}"
    

def convert_to_midi(wave_output_file, midi_output, silence_threshold=-40.0):
    signal, sr = librosa.load(wave_output_file, sr=None)

    # calculate the RMS energy of the signal, to diff singing and noise...
    rms = librosa.feature.rms(y=signal, frame_length=2048, hop_length=512)
    rms_db = librosa.amplitude_to_db(rms, ref=np.max)

    fmin = librosa.note_to_hz('C2')
    fmax = librosa.note_to_hz('C7')
    pitches, voiced_flags, _ = librosa.pyin(signal, fmin=fmin, fmax=fmax, sr=sr)

    midi_file = MidiFile()
    track = MidiTrack()
    midi_file.tracks.append(track)

    hop_length = 512
    ticks_per_beat = midi_file.ticks_per_beat
    onset_env = librosa.onset.onset_strength(y=signal, sr=sr) # to future me, https://librosa.org/doc/0.11.0/generated/librosa.onset.onset_strength.html#librosa.onset.onset_strength

    # using the librosa beat detection function, rather than hardcoding it...
    estimated_tempo = librosa.feature.tempo(y=signal, sr=sr)[0] # need to make scalar, else gives error on // to BPS
    print(estimated_tempo) 
    if estimated_tempo == 0 or np.isnan(estimated_tempo):
        estimated_tempo = 120.0  # fallback for weird cases like whispering


    last_pitch = None
    last_time = 0

    for i, (pitch, voiced_flag) in enumerate(zip(pitches, voiced_flags)):
        rms_value = rms_db[0][i]
        if voiced_flag and rms_value > silence_threshold:
            tempo_bpm = estimated_tempo
            microseconds_per_beat = int(60_000_000 / tempo_bpm)
            ticks_per_second = (ticks_per_beat * 1_000_000) // microseconds_per_beat

            midi_note = freq_to_midi(pitch)
            current_time = int((i * hop_length) / sr * ticks_per_second)

            if last_pitch is not None and last_pitch != midi_note:
                # note off for the previous note
                duration = current_time - last_time
                if duration < 0:
                    duration = 0
                track.append(Message('note_off', note=last_pitch, velocity=64, time=duration))
                last_time = current_time

            # note on for the current note
            if last_pitch != midi_note:
                track.append(Message('note_on', note=midi_note, velocity=64, time=0))
                last_pitch = midi_note
                last_time = current_time

                alphabet = midi_to_alphabet(midi_note)
                if alphabet:
                    print(f"Pitch: {pitch:.2f}, MIDI Note: {alphabet}")
                else:
                    print(f"No alphabet mapping found for MIDI Note {midi_note}")

     # note off for the last note
    if last_pitch is not None:
        track.append(Message('note_off', note=last_pitch, velocity=64, time=0))

    # save the masterpiece ;)
    midi_file.save(midi_output)
    print(f"Saved MIDI to {midi_output}")
