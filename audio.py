import pygame
from random import randint


class Audio():
    def __init__(self):
        pygame.mixer.set_num_channels(16)
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        self.bg_sound = pygame.mixer.music.load("audiofiles/soundtrack.ogg")

    def play_background(self):  #Background music
        pygame.mixer.music.play(-1)
        # self.bg_sound.play(-1)
    def pussy(self):    #Grab em by the pussy sound
        a = pygame.mixer.Sound("audiofiles/pussygrab.ogg")
        pygame.mixer.Sound.play(a)
    def hit(self):  #Hit sounds
        a = pygame.mixer.Sound("audiofiles/hit0.ogg")
        b = pygame.mixer.Sound("audiofiles/hit1.ogg")
        c = pygame.mixer.Sound("audiofiles/hit2.ogg")
        d = pygame.mixer.Sound("audiofiles/hit3.ogg")
        e = pygame.mixer.Sound("audiofiles/hit4.ogg")

        if chance == 0:
            pygame.mixer.Sound.play(a)
        elif chance == 1:
            pygame.mixer.Sound.play(b)
        elif chance == 2:
            pygame.mixer.Sound.play(c)
        elif chance == 3:
            pygame.mixer.Sound.play(d)
        elif chance == 4:
            pygame.mixer.Sound.play(e)
    def jump(self): #Jump sound
        a = pygame.mixer.Sound("audiofiles/jump.ogg")
        pygame.mixer.Sound.play(a)

    def trumpwin(self): #Trump win sound
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
    def clintonwin(self):   #Clinton win sound
        chance = randint(0, 2)

        a = pygame.mixer.Sound("audiofiles/clintonwin0.ogg")
        b = pygame.mixer.Sound("audiofiles/clintonwin1.ogg")

        if chance == 0:
            pygame.mixer.Sound.play(a)
        elif chance == 1:
            pygame.mixer.Sound.play(b)



