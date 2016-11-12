import pygame
import constants

class LowerPlatform():
    def __init__(self, x, y, w, h):
        self.x = x -25
        self.y = y
        self.rect = pygame.Rect([x, y, w, h])
        self.color = [255, 0, 0]
        self.rectangle = pygame.Rect([self.x, self.y, 0, 0])

        self.blit = pygame.image.load('art_assets/lava_alumine.png')
    def draw(self, s):
        s.blit(self.blit, self.rectangle)


class UpperPlatform():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.rect = pygame.Rect([x, y, w, h])
        self.color = [255, 0, 0]
        self.blit = pygame.image.load("art_assets/lava_ylemine - Copy.png")
        self.rectangle = pygame.Rect([self.x, self.y, 0, 0])
    def draw(self, s):
        s.blit(self.blit, self.rectangle)

background = pygame.image.load("taust.png")