import pygame
from constants import *
import sys

if __name__ == '__main__':
    screen = pygame.display.set_mode(RESOLUTION, pygame.FULLSCREEN)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()