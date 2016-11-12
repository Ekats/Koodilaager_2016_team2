import pygame

class Audio():
    def __init__(self):
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        self.bg_sound = pygame.mixer.music.load("audiofiles/soundtrack.ogg")

    def play_background(self):
        pygame.mixer.music.play()
        # self.bg_sound.play(-1)
