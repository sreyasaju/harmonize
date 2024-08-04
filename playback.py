from pydub import AudioSegment
from pydub.playback import play

def play_wav_file(wave_output_file):
    audio = AudioSegment.from_wav(wave_output_file)
    play(audio)

