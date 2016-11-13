#Raido Rehepapp tegi



import pygame
from constants import *
import sys
import player
import player2
import map
import audio


trump_char = player.CharTrump(100, 110)
clinton_char = player2.CharClinton(284, 110)
platforms = (
    map.LowerPlatform(100, 145, 200, 80),
    map.UpperPlatform(50, 70, 100, 10),
    map.UpperPlatform(250, 70, 100, 10),
    #map.LowerUPlatform(100, 145, 200, 80),
)

trump_hits = []
clinton_hits = []

if __name__ == '__main__':
    pygame.init()

    pause = False

    window = pygame.display.set_mode(RESOLUTION)
    screen = pygame.Surface([400, 225])
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

                if e.key == pygame.K_m:
                    if not pause:
                        pygame.mixer.music.pause()
                        pause = True
                    else:
                        pygame.mixer.music.unpause()
                        pause = False

            trump_char.event_handle(e, screen, trump_hits)
            clinton_char.event_handle(e, screen, clinton_hits)

        screen.fill([0, 0, 0])
        screen.blit(map.background, [0, 0])
        screen.blit(banner_l, [10, 10])
        screen.blit(banner_r, [270, 10])
        screen.blit(stage_upper, [100, 125])

        for i in platforms:
            trump_char.collide(i)
            i.draw(screen)

        for i in platforms:
            clinton_char.collide(i)
            i.draw(screen)

        trump_char.get_hit(clinton_hits, clinton_char)
        clinton_char.get_hit(trump_hits, trump_char)

        trump_char.update()
        trump_char.draw(screen)
        clinton_char.update()
        clinton_char.draw(screen)
        screen.blit(stage_lower, [75, 145])

        screen_scaled = pygame.transform.scale(screen, RESOLUTION)
        window.blit(screen_scaled, [0, 0])

        pygame.display.flip()
        ms = clock.tick(30)
