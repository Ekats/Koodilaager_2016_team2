import pygame
import main
import constants
import player

class lowerplatform():
    def draw_lower(self):
        PlatformObject_below = pygame.Rect([100, 145, 200, 800])
        pygame.draw.rect(screen, [0, 0, 0], PlatformObject_below)

    player.collide(Trump, lowerplatform)

class upperplatforms():
    def draw_upper(self):
        PlatformObject_1 = pygame.Rect([50, 70, 100, 10])
        PlatformObject_2 = pygame.Rect([250, 70, 100, 10])
        upperplatforms = [PlatformObject_1, PlatformObject_2]

        for part in upperplatforms:
            upperplatforms.draw(screen)
            player.collide(Trump, part)
