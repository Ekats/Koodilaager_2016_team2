import pygame
from function_hitback import *
import audio

audio_manager = audio.Audio()

class CharTrump():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_spd = 0
        self.y_vel = 0
        self.max_spd = 8
        self.max_vel = 18
        self.color = [255, 0, 0]
        self.rectangle = pygame.Rect([self.x, self.y, 16, 30])
        self.dir = 1
        self.hitbox = pygame.Rect([self.x-2, self.y, 20, 30])
        self.jumps_remaining = 1
        self.acc = 0
        self.lives = 3

        self.in_air = False
        self.left = False
        self.right = False

        self.dam = 5

        self.blit_stand = pygame.image.load("art_assets/trump_stand.png")
        self.blit_walk = pygame.image.load("art_assets/trump_walk.png")
        self.blit_jump = pygame.image.load("art_assets/trump_jump.png")
        self.blit_walk_left = pygame.image.load("art_assets/trump_walk_left.png")
        self.blit_stand_left = pygame.image.load("art_assets/trump_walk1_left.png")
        self.blit_jump_left = pygame.image.load("art_assets/trump_jumpL.png")
        self.life = pygame.image.load("art_assets/hearth.png")

    def draw(self, s):

        if self.dir == 1 and self.x_spd == 0 and not self.in_air:
            s.blit(self.blit_stand, self.rectangle)
        elif self.dir == 3 and self.x_spd == 0:
            s.blit(self.blit_stand_left, self.rectangle)

        if self.dir == 1 and self.x_spd < 0 or self.x_spd > 0:
            s.blit(self.blit_walk, self.rectangle)
        elif self.dir == 3 and self.x_spd < 0 or self.x_spd > 0:
            s.blit(self.blit_walk_left, self.rectangle)

        elif self.dir == 1 and self.in_air == True:
            s.blit(self.blit_jump, self.rectangle)
        elif self.dir == 3 and self.in_air == True:
            s.blit(self.blit_jump_left, self.rectangle)

        if self.lives > 2:
            s.blit(self.life, [22, 12])
        if self.lives > 1:
            s.blit(self.life, [42, 12])
        if self.lives > 0:
            s.blit(self.life, [62, 12])

    def jump(self, vel):
        self.y_vel = -vel
        self.in_air = True

    def move(self, spd):
        if self.x_spd < self.max_spd and self.x_spd > -self.max_spd:
            self.x_spd += spd

    """def hit1(self, target_hitbox, self.dam):
    if self.rectangle.colliderect(target_hitbox):
        self.dam = self.dam * 5
        self.x_spd += self.dam
        self.x += self.x_spd
        if self.x_spd > 0:
            self.x_spd -= 1"""

    #if lause, kinnitus, et teine karakter lõi
    #mingi arv + self.dam (erinev kick liidab erinevaid arve)
    #löögist tulenev lendamine * self.dam


    """def kick1(self, hitbox_position, hits_list):
        hits_list.append(hitbox_position)"""

        #insert blit,blit peaks olema hitboxi suurune, paneme hitboxi peale, kontrollime suunda, sound
        #kui mingit nuppu vajutab siis kontrolli, kas vastane hitboxi sees
        #cooldown kuhugi
        #return

    def kick2(self):
        pass

    def kickspecial(self):
        pass

    def reset_pos(self):
        self.y = 110
        self.x = 100

    def update(self):

        if self.y_vel < self.max_vel:
            self.y_vel += 2

            self.rectangle.y += 1

        if self.rectangle.y > 1200 and self.lives > 0:
            self.reset_pos()
            self.lives -= 1

        if self.x_spd > 0:
            self.x_spd -= 1
        if self.x_spd < 0:
            self.x_spd += 1
        if (self.x_spd + self.acc) < self.max_spd and (self.x_spd + self.acc) > -self.max_spd:
            self.x_spd += self.acc

        self.y += self.y_vel
        self.x += self.x_spd

        self.rectangle = pygame.Rect([self.x, self.y, 16, 30])

    def collide(self, target):
        if self.rectangle.colliderect(target.rect) and self.y_vel > 0 and self.rectangle.center[1] < target.rect.center[1]:
            self.y = target.rect.y - self.rectangle.h
            self.y_vel = 0
            self.jumps_remaining = 1
            self.in_air = False

    def event_handle(self, event, s, hits_list):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and self.jumps_remaining > 0:
                self.jump(20)
                self.jumps_remaining -= 2
                audio_manager.trumpjump()

            if event.key == pygame.K_d:
                self.dir = 1
                self.acc = 2
                self.right = True

            elif event.key == pygame.K_a:
                self.dir = 3
                self.acc = -2
                self.left = True

            if event.key == pygame.K_c:
                hits_list.append(kick1(pygame.Rect([self.x-2, self.y, 20, 30]), 50))

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.dir = 1
                if self.right == False:
                    self.acc = 0
                self.right = False

            elif event.key == pygame.K_a:
                self.dir = 3
                if self.left == False:
                    self.acc = 0
                self.left = False

            if self.left == False and self.right == False:
                self.acc = 0

    def get_hit(self, hits_list, opponent):
        for i in hits_list:
            if self.rectangle.colliderect(i.rect):
                hit1(self, self.dam, opponent)

        del hits_list[:]

