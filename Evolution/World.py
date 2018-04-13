import simpy
from Food import Food
from Organism import Organism
import random
import pygame

class World():
    def __init__(self, ecosystem, env, screen, display, image, event):

        self.ecosystem  = ecosystem
        self.env        = env
        self.screen     = screen
        self.display    = display
        self.image      = image
        self.event      = event
        self.count      = 0

        # for org in organisms:
        #     org_img         = image.load("organism.bmp")
        #     org_rect        = org_img.get_rect()
        #     org_rect.y      = 750
        #     org_rect.x      = 100 * organisms.index(org)
        #     #org.set_rect(org_rect)
        #     #org.set_img(org_img)
        #
        # count = 0
        # for food in foods:
        #     food_img	= image.load("food.bmp")
        #     food_rect	= food_img.get_rect()
        #     food.rect	= food_rect
        #     food.img	= food_img
        #     count+=1

        for event in self.event.get():
            if event.type == pygame.QUIT: sys.exit()
        black = 255, 255, 255
        self.screen.fill(black)
    def run(self):
        while True:
            self.count+=1
            # for ele in self.foods:
            #     print(ele.get_name(),end = " ")
            print((str(self.count)), end = ". ")
            for being in self.ecosystem.all_beings():
                print(being.get_name(), end = " ")
            print(" "+ str(len(self.ecosystem.all_beings())))

            self.display.flip()
            yield self.env.timeout(1)
