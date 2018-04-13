__author__ = "Jeffrey Lin"

""" This project is designed for simulating organisms and
attempting to simulate evolution
"""

import random
import simpy
import pygame
from Organism   import Organism
from Food       import Food
from World      import World
from Ecosystem  import Ecosystem

RANDOM_SEED             = 42
START_NUM_OF_ORGANISMS  = 1
NUM_OF_FOOD             = 3

## Create simpy env and start pygame
env = simpy.RealtimeEnvironment(initial_time=0, factor=0.1, strict=False)
pygame.init()
print("Starting simulation")

ecosystem = Ecosystem()

size = width, height = 1000, 800
screen  = pygame.display.set_mode(size)
display = pygame.display
image   = pygame.image
event   = pygame.event

for org in range(START_NUM_OF_ORGANISMS):
    new_org = Organism("O-" + str(org), ecosystem, env)
    ecosystem.add_being(new_org)

for food in range(NUM_OF_FOOD):
    new_food = Food("F-" + str(food), ecosystem, env)
    ecosystem.add_being(new_food)

Emerge = World(ecosystem, env, screen, display, image, event)

##TODO: Attempt to minimilize code by combining this part with above when initializing the organisms/food

for being in ecosystem.all_beings():
    env.process(being.run())

env.process(Emerge.run())
env.run(until = 100)

print("Simulation End")
