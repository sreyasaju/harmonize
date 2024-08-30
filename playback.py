import pygame

class playAudio:
    def __init__(self, wave_output_file):
        pygame.mixer.init()
        self.file_path = wave_output_file
        pygame.mixer.music.load(wave_output_file)
        self.is_playing = False
        self.is_paused = False

    def play(self):
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
        else:
            pygame.mixer.music.play()
            self.is_playing = True

    def pause(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_paused = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused = False