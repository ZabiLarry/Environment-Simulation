import pygame


class Creature:

    def __init__(self, color, x, y, size, speed, energy, range, next_moves=[]):
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.energy = energy
        self.hitbox = size + range
        self.range = range
        self.next_moves = next_moves

    def move(self, direction):
        if direction == 1:  # move right
            if self.x < 890 - self.size:
                self.x += self.speed
        if direction == 2:  # move up
            if self.y > 10 + self.size:
                self.y -= self.speed
        if direction == 3:  # move left
            if self.x > 10 + self.size:
                self.x -= self.speed
        if direction == 4:  # move down
            if self.y < 890 - self.size:
                self.y += self.speed
        self.energy -= (self.speed + self.range / 10) / 40
