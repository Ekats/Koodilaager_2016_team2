import pygame
from constants import *
import sys
import player
import map
import audio

trump_char = player.CharTrump(100, 110)
platforms = [
    map.LowerPlatform(100, 145, 200, 80),
    map.UpperPlatform(50, 70, 100, 10),
    map.UpperPlatform(250, 70, 100, 10)
]

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode(RESOLUTION)
    clock = pygame.time.Clock()

    audio_manager = audio.Audio()
    audio_manager.play_background()
    # audio_manager.pussy()
    # audio_manager.trumpwin()
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

        for i in platforms:
            trump_char.collide(i)
            i.draw(screen)

        trump_char.update()
        trump_char.draw(screen)

        pygame.display.flip()
        ms = clock.tick(30)