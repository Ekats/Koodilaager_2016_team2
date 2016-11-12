import pygame

class CharTrump():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_spd = 0
        self.y_vel = 0
        self.max_spd = 12
        self.max_vel = 18
        self.color = [255, 0, 0]
        self.rectangle = pygame.Rect([self.x, self.y, 16, 16])

    def draw(self, s):
        pygame.draw.rect(s, self.color, self.rectangle)

    def jump(self, vel):
        self.y_vel = -vel

    def move(self, spd):
        if self.x_spd < self.max_spd and self.x_spd > -self.max_spd:
            self.x_spd += spd

    def kick1(self):
        pass


    def update(self):
        if self.x_spd > 0:
            self.x_spd -= 1

        elif self.x_spd < 0:
            self.x_spd += 1

        if self.y_vel < self.max_vel:
            self.y_vel += 4

        self.y += self.y_vel
        self.x += self.x_spd

        self.rectangle = pygame.Rect([self.x, self.y, 16, 16])

    def collide(self, target):
        while pygame.Rect([self.x, self.y + self.y_vel, 16, 16]).colliderect(target):
            if self.y_vel > 0:
                self.y_vel -= 1
            if self.y_vel < 0:
                self.y_vel += 1
            #self.rectangle = pygame.Rect([self.x, self.y, 16, 16])

        while pygame.Rect([self.x + self.x_spd, self.y + self.y_vel, 16, 16]).colliderect(target):
            if self.x_spd > 0:
                self.x_spd -= 1
            if self.x_spd < 0:
                self.x_spd += 1

