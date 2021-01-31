import pygame
import os
import time
import random as rand
from Creature import Creature
from Food import Food

pygame.init()
WIDTH = 900
HEIGHT = 900

win = pygame.display.set_mode((WIDTH, HEIGHT))
CREATURE_AMOUNT = 10
FOOD_AMOUNT = 15

pygame.display.set_caption("Environment Simulator")

creatures = []
foods = []


def draw_creature():
    pygame.draw.circle(win, creature.color, (creature.x, creature.y), creature.size)  # creature
    pygame.draw.circle(win, (100, 100, 100), (creature.x, creature.y), creature.hitbox, 2)  # hitbox


def create_creatures():
    for i in range(CREATURE_AMOUNT):  # summon creatures
        randx = rand.randint(0, WIDTH)
        randy = rand.randint(0, HEIGHT)
        creature = Creature((200, 0, 0), randx, randy, 5, 5, 70, 10)
        draw_creature()
        creatures.append(creature)


def create_food():
    for i in range(FOOD_AMOUNT):  # summon food
        randx = rand.randint(0, WIDTH)
        randy = rand.randint(0, HEIGHT)
        food = Food((100, 100, 10), randx, randy, 3)
        pygame.draw.circle(win, food.color, (food.x, food.y), food.size)  # food
        foods.append(food)


create_food()
create_creatures()

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((50, 105, 30))
    for creature in creatures:
        randmove = rand.randint(1, 4)
        if randmove == 1:
            creature.moveRight()
            creature.moveRight()
        elif randmove == 2:
            creature.moveLeft()
            creature.moveLeft()
        elif randmove == 3:
            creature.moveUp()
            creature.moveUp()
        elif randmove == 4:
            creature.moveDown()
            creature.moveDown()
        draw_creature()

    pygame.display.update()
