import pygame
import player
import player2

def hit1(self, target, target.dam):
    target.dam = target.dam * 5
    target.x_spd += target.dam
    target.x += target.x_spd
    if target.x_spd > 0:
        self.x_spd -= 1

def hit2(self, target, target.dam):
    target.dam = target.dam * 8
    target.x_spd += target.dam
    target.x += target.x_spd
    if target.x_spd > 0:
        self.x_spd -= 2

def hitspecial(self, target, target.dam):
    target.dam = target.dam * 200
    target.x_spd += target.dam
    target.x += target.x_spd
    if target.x_spd > 0:
        self.x_spd -= 3
