import pygame
import os
import time
import random as rand
from Creature import Creature
from Food import Food

pygame.init()
WIDTH = 900
HEIGHT = 900
font = pygame.font.SysFont('arial', 16)

win = pygame.display.set_mode((WIDTH, HEIGHT))
CREATURE_AMOUNT = 5
FOOD_AMOUNT = 50

pygame.display.set_caption("Environment Simulator")

creatures = []
foods = []


def draw_creature(creature):
    pygame.draw.circle(win, creature.color, (creature.x, creature.y), creature.size)  # creature
    pygame.draw.circle(win, (100, 100, 100), (creature.x, creature.y), creature.hitbox, 2)  # hitbox
    pygame.draw.rect(win, (200, 0, 0), (creature.x - 6, creature.y - 10, 12, 2))  # energy bar empty
    pygame.draw.rect(win, (0, 200, 0), (creature.x - 6, creature.y - 10, (creature.energy / 8), 2))  # energy bar full


def draw_food(food):
    pygame.draw.circle(win, food.color, (food.x, food.y), food.size)  # draw food


def create_creatures(amount):
    for i in range(amount):  # summon creatures
        randx = rand.randint(0, WIDTH - 10)
        randy = rand.randint(0, HEIGHT - 10)
        creature = Creature((randx / 4, randy / 4, (randx + randy) / 8), randx, randy, 5, 5, 100, 100)  # speed cannot be greater than size
        draw_creature(creature)
        creatures.append(creature)


def create_food():
    for i in range(FOOD_AMOUNT):  # summon food
        randx = rand.randint(0, WIDTH - 10)
        randy = rand.randint(0, HEIGHT - 10)
        rands = rand.randint(3, 4)
        food = Food((220, 120, 10), randx, randy, rands)
        draw_food(food)
        foods.append(food)


def make_baby(parent):
    mutate = rand.randint(1, 5)
    newrange = parent.range
    newspeed = parent.speed
    if mutate == 1:
        mutation = rand.randint(1, 4)
        if mutation < 3:
            if mutation == 1:
                newrange = parent.range + 2
            else:
                newrange = parent.range - 2
        else:
            if mutation == 3:
                newspeed = parent.speed + 2
            else:
                newspeed = parent.speed - 2

    baby = Creature(parent.color, parent.x, parent.y, parent.size, newspeed, parent.energy / 2, newrange)
    creatures.append(baby)
    draw_creature(baby)



create_food()
create_creatures(CREATURE_AMOUNT)

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((50, 105, 30))
    for creature in creatures:
        move = rand.randint(1, 4)
        if len(creature.next_moves) > 0:  # check if must go for food
            move = creature.next_moves[0]
            creature.next_moves.pop(0)
            creature.do_move = False

        creature.move(move)
        for food in foods:
            if creature.y + creature.hitbox > food.y > creature.y - creature.hitbox and creature.x + creature.hitbox > food.x > creature.x - creature.hitbox:
                creature.energy = creature.energy + food.size * 30  # eat food
                foods.remove(food)# finds food
                if creature.energy > creature.size ** 3:
                    make_baby(creature)
                creature.energy = creature.energy / 2
                if creature.y + creature.size > food.y > creature.y - creature.size and creature.x + creature.size > food.x > creature.x - creature.size:
                    '''elif len(creature.next_moves)==0:  # get to food
                    creature.do_move = True
                    movesx = round((food.x - creature.x)/creature.speed)
                    movesy = round((food.y - creature.y)/creature.speed)
                    if movesx < 0:
                        movesx = abs(movesx)
                        for i in range(movesx):
                            creature.next_moves.append(3)
                    else:
                        for i in range(movesx):
                            creature.next_moves.append(1)
                    if movesy < 0:
                        movesy = abs(movesy)
                        for i in range(movesy):
                            creature.next_moves.append(2)
                    else:
                        for i in range(movesy):
                            creature.next_moves.append(4)'''

            draw_food(food)
            draw_creature(creature)


        if creature.energy < 1:  # die
            creatures.remove(creature)
            deadBody = Food((100, 0, 0), creature.x, creature.y, creature.size/2)
            draw_food(deadBody)
            foods.append(deadBody)


    text = font.render("Creatures:" + str(len(creatures)), 1, (0, 0, 0))
    win.blit(text, (820, 5))
    pygame.display.update()
