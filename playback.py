from pydub import AudioSegment
from pydub.playback import play
import pygame.midi
from mido import MidiFile

def play_wav_file(wave_output_file):
    audio = AudioSegment.from_wav(wave_output_file)
    play(audio)

def play_midi_file(midi_output):
    pygame.midi.init()
    player = pygame.midi.Output(1)
    midi = MidiFile(midi_output)

    for msg in midi.play():
        if not msg.is_meta:
            if msg.type == 'note_on':
                player.note_on(msg.note, msg.velocity)
            elif msg.type == 'note_off':
                player.note_off(msg.note, msg.velocity)
    player.close()
    pygame.midi.quit()