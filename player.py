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
        self.rectangle = pygame.Rect([self.x, self.y, 16, 30])
        self.dir = 1

    def draw(self, s):
        pygame.draw.rect(s, self.color, self.rectangle)



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
            #self.rectangle = pygame.Rect([self.x, self.y, 16, 30])

        while pygame.Rect([self.x + self.x_spd, self.y + self.y_vel, 16, 16]).colliderect(target):
            if self.x_spd > 0:
                self.x_spd -= 1
            if self.x_spd < 0:
                self.x_spd += 1

    def event_handle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.jump(20)

            if event.key == pygame.K_d:
                self.x_spd = 8

            elif event.key == pygame.K_a:
                self.x_spd = -8

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.dir = 1
                self.x_spd = 0

            if event.key == pygame.K_a:
                self.dir = 3
                self.x_spd = 0
