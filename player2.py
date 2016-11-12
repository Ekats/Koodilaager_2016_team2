import pygame
import audio

audio_manager = audio.Audio()


class CharClinton():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_spd = 0
        self.y_vel = 0
        self.max_spd = 12
        self.max_vel = 18
        self.color = [0, 0, 255]
        self.rectangle = pygame.Rect([self.x, self.y, 16, 30])
        self.dir = 1
        self.hitbox = pygame.Rect([self.x-2, self.y, 18, 30])
        self.blit = pygame.image.load("art_assets/hillary_stand.png")


    def draw(self, s):
        s.blit(self.blit, self.rectangle)

    def jump(self, vel):
        self.y_vel = -vel

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

        #if self.rectangle.colliderect(target.rect) and self.y_vel < 0:
            #print(8)

    def event_handle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.jump(20)
                audio_manager.jump()

            if event.key == pygame.K_RIGHT:
                self.x_spd = 8

            elif event.key == pygame.K_LEFT:
                self.x_spd = -8

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.dir = 1
                self.x_spd = 0

            if event.key == pygame.K_LEFT:
                self.dir = 3
                self.x_spd = 0
