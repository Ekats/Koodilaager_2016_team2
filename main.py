import pygame
from constants import *
import sys
import player
import map

trump_char = player.CharTrump(100, 200)


if __name__ == '__main__':
    screen = pygame.display.set_mode(RESOLUTION, pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    # ms is milliseconds passed since last frame
    ms = clock.tick(30)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            trump_char.event_handle(e)


        screen.fill([0, 0, 0])

        map.lowerplatform.draw_lower()
        map.upperplatforms.draw_upper()

        trump_char.update()
        trump_char.draw(screen)

        pygame.display.flip()
        ms = clock.tick(30)