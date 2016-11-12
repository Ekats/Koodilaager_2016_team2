import pygame
from random import randint


class Audio():
    def __init__(self):
        pygame.mixer.set_num_channels(16)
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        self.bg_sound = pygame.mixer.music.load("audiofiles/soundtrack.ogg")

    def play_background(self):
        pygame.mixer.music.play(-1)
        # self.bg_sound.play(-1)
    def pussy(self):
        a = pygame.mixer.Sound("audiofiles/pussygrab.ogg")
        pygame.mixer.Sound.play(a)
    def trumpwin(self):
        chance = randint(0, 2)

        a = pygame.mixer.Sound("audiofiles/trumpwin0.ogg")
        b = pygame.mixer.Sound("audiofiles/trumpwin1.ogg")
        c = pygame.mixer.Sound("audiofiles/trumpwin2.ogg")

        if chance == 0:
            pygame.mixer.Sound.play(a)
        elif chance == 1:
            pygame.mixer.Sound.play(b)
        elif chance == 2:
            pygame.mixer.Sound.play(c)
    def clintonwin(self):
        chance = randint(0, 2)

        a = pygame.mixer.Sound("audiofiles/clintonwin0.ogg")
        b = pygame.mixer.Sound("audiofiles/clintonwin1.ogg")

        if chance == 0:
            pygame.mixer.Sound.play(a)
        elif chance == 1:
            pygame.mixer.Sound.play(b)



