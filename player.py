import pygame
import audio


audio_manager = audio.Audio()
#jumps_remaining = 2

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
        self.blit_stand = pygame.image.load("art_assets/trump_stand.png")
        self.blit_walk = pygame.image.load("art_assets/trump_walk.png")
        self.blit_jump = pygame.image.load("art_assets/trump_jump.png")
        self.blit_stand_left = pygame.image.load("art_assets/trump_stand_left.png")
        self.blit_walk_left = pygame.image.load("art_assets/trump_walk_left.png")
        self.blit_jump_left = pygame.image.load("art_assets/trump_jump_left.png")

    def draw(self, s):

        if self.dir == 1 and self.x_spd < 0 or self.x_spd > 0:
            s.blit(self.blit_walk, self.rectangle)
        elif self.dir == 3 and self.x_spd < 0 or self.x_spd > 0:
            s.blit(self.blit_walk_left, self.rectangle)

        elif self.y_vel < 2 or self.y_vel > 2:
            s.blit(self.blit_jump, self.rectangle)
            print(self.y_vel)
        else:
            s.blit(self.blit_stand, self.rectangle)

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
            #global jumps_remaining = 2

    def event_handle(self, event, s):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.jump(20)
                s.blit(self.blit_jump, self.rectangle)
                #global jumps_remaining -= 1
                audio_manager.trumpjump()

            if event.key == pygame.K_d:
                self.x_spd = 8
                self.dir = 1

            elif event.key == pygame.K_a:
                self.x_spd = -8
                self.dir = 3

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.dir = 1
                self.x_spd = 0

            if event.key == pygame.K_a:
                self.dir = 3
                self.x_spd = 0
