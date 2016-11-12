import pygame

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
        a = pygame.mixer.Sound("audiofiles/trumpwin0.ogg")
        b = pygame.mixer.Sound("audiofiles/trumpwin1.ogg")
        c = pygame.mixer.Sound("audiofiles/trumpwin2.ogg")

        pygame.mixer.Sound.play(a or b or c)
