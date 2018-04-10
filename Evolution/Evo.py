__author__ = "Jeffrey Lin"

""" This project is designed for simulating organisms and
attempting to simulate evolution
"""

import random
import simpy
import pygame
from Organism import Organism
from Food import Food
from World import World

RANDOM_SEED             = 42
START_NUM_OF_ORGANISMS  = 1
NUM_OF_FOOD             = 3

## Create simpy env and start pygame
env = simpy.RealtimeEnvironment(initial_time=0, factor=0.1, strict=False)
pygame.init()

organisms   = []
foods       = []

size = width, height = 1000, 800
screen  = pygame.display.set_mode(size)
display = pygame.display
image   = pygame.image
event   = pygame.event

for org in range(START_NUM_OF_ORGANISMS):
	new_org = Organism("O-" + str(org), env)
	organisms.append(new_org)

for food in range(NUM_OF_FOOD):
    new_food = Food("F-" + str(food), env)
    foods.append(new_food)

Emerge = World(organisms, foods, env, screen, display, image, event)

##TODO: Attempt to minimilize code by combining this part with above when initializing the organisms/food
for org in organisms:
    env.process(org.run())

for food in foods:
    env.process(food.run())

env.process(Emerge.run())
env.run(until= 100)
