import pygame

class kick1:
    def __init__(self, rect, dmg):
        self.rect = rect
        self.dmg = dmg
        self.type = 1

def hit1(self, dam, opponent):
    self.dam = self.dam + 2
    self.x_spd = self.dam + self.x_spd
    if opponent.x < self.x:
        self.x += self.x_spd
        if self.x_spd > 0:
            self.x_spd -= 2
    if opponent.x > self.x:
        self.x_spd = -self.x_spd
        self.x += self.x_spd
        if self.x_spd < 0:
            self.x_spd += 2

class kick2:
    def __init__(self, rect, dmg):
        self.rect = rect
        self.dmg = dmg
        self.type = 2

def hit2(self, dam, opponent):
    self.dam = self.dam + 8
    self.x_spd = self.dam + self.x_spd
    if opponent.x < self.x:
        self.x += self.x_spd
        if self.x_spd > 0:
            self.x_spd -= 2
    if opponent.x > self.x:
        self.x_spd = -self.x_spd
        self.x += self.x_spd
        if self.x_spd < 0:
            self.x_spd += 2

class kickspecial:
    def __init__(self, rect, dmg):
        self.rect = rect
        self.dmg = dmg
        self.type = 3

def hitspecial(self, dam, opponent):
    self.dam = self.dam + 10
    self.x_spd = self.dam + self.x_spd
    if opponent.x < self.x:
        self.x += self.x_spd
        if self.x_spd > 0:
            self.x_spd -= 2
    if opponent.x > self.x:
        self.x_spd = -self.x_spd
        self.x += self.x_spd
        if self.x_spd < 0:
            self.x_spd += 2
