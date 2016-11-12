import pygame
import constants

class LowerPlatform():
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect([x, y, w, h])
        self.color = [255, 0, 0]

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class UpperPlatform():
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect([x, y, w, h])
        self.color = [255, 0, 0]

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)