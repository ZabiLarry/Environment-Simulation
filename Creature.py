import pygame


class Creature:

    def __init__(self, color, x, y, size, speed, energy, range):
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.energy = energy
        self.hitbox = size + range

    def moveLeft(self):
        if self.x > 0 + self.size:
            self.x -= self.speed

    def moveRight(self):
        if self.x < 900 - self.size:
            self.x += self.speed

    def moveUp(self):
        if self.y > 0 + self.size:
            self.y -= self.speed

    def moveDown(self):
        if self.y < 900 - self.size:
            self.y += self.speed
