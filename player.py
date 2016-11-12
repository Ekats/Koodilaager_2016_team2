import pygame
import audio

audio_manager = audio.Audio()

class CharTrump():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_spd = 0
        self.y_vel = 0
        self.max_spd = 12
        self.max_vel = 18
        self.color = [255, 0, 0]
        self.rectangle = pygame.Rect([self.x, self.y, 16, 30])
        self.dir = 1
        self.hitbox = pygame.Rect([self.x-2, self.y, 18, 30])
        self.blit = pygame.image.load("art_assets/trump_stand.png")
        self.jumps_remaining = 2

        self.in_air = False
        self.horizontal_movement = False

        self.blit_stand = pygame.image.load("art_assets/trump_stand.png")
        self.blit_walk = pygame.image.load("art_assets/trump_walk.png")
        self.blit_jump = pygame.image.load("art_assets/trump_jump.png")


    def draw(self, s):
        if self.in_air:
            s.blit(self.blit_jump, self.rectangle)
        elif self.horizontal_movement:
            s.blit(self.blit_walk, self.rectangle)
        else:
            s.blit(self.blit_stand, self.rectangle)

    def jump(self, vel):
        self.y_vel = -vel
        self.in_air = True

    def move(self, spd):
        if self.x_spd < self.max_spd and self.x_spd > -self.max_spd:
            self.x_spd += spd

    def kick1(self):
        pass

    def kick2(self):
        pass

    def kickspecial(self):
        pass

    def update(self):
        if self.y_vel < self.max_vel:
            self.y_vel += 2

        self.y += self.y_vel
        self.x += self.x_spd

        self.rectangle = pygame.Rect([self.x, self.y, 16, 30])

    def collide(self, target):
        if self.rectangle.colliderect(target.rect) and self.y_vel > 0 and self.rectangle.center[1] < target.rect.center[1]:
            self.y = target.rect.y - self.rectangle.h
            self.y_vel = 0
            self.jumps_remaining = 2
            self.in_air = False

    def event_handle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and self.jumps_remaining > 0:
                self.jump(20)

                self.jumps_remaining -= 1

                audio_manager.trumpjump()

            if event.key == pygame.K_d:
                self.x_spd = 8
                self.horizontal_movement = True

            elif event.key == pygame.K_a:
                self.x_spd = -8
                self.horizontal_movement = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.dir = 1
                self.x_spd = 0
                self.horizontal_movement = False

            if event.key == pygame.K_a:
                self.dir = 3
                self.x_spd = 0
                self.horizontal_movement = False
