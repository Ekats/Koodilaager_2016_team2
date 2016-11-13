import pygame

class kick1:
    def __init__(self, rect, dmg):
        self.rect = rect
        self.dmg = dmg

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

"""def hit2(self, target, target.dam):
    target.dam = target.dam + 8
    target.x_spd += target.dam
    target.x += target.x_spd
    if target.x_spd > 0:
        self.x_spd -= 2

def hitspecial(self, target, target.dam):
    target.dam = target.dam + 200
    target.x_spd += target.dam
    target.x += target.x_spd
    if target.x_spd > 0:
        self.x_spd -= 3"""
