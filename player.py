# system modules
import pygame
import random
import sys
# local modules
from player import *
from monster import *
from item import *
from background import *
from world import *
from animation import *
from constants import *


class Player(object):
    """class Player, for the game character. It will download the progress using something else than pickle"""

    def __init__(self):

        # inheritate constructor
        super().__init__()

        # set images
        self.images = {
            'run': [
                pygame.image.load('assets/images/player/sticky/run1.png'),
                pygame.image.load('assets/images/player/sticky/run2.png'),
                pygame.image.load('assets/images/player/sticky/run3.png')
            ],
            'stand': [pygame.image.load('assets/images/player/sticky/stand.png')],
            'jump': [pygame.image.load('assets/images/player/sticky/jump.png')],
            'dead': [pygame.image.load('assets/images/player/sticky/dead.png')]
        }

        for key in self.images:
            for image in self.images[key]:
                image.set_colorkey((0,0,0))
                image.convert()

        self.rect = self.images['run'][0].get_rect()

        self.rect.x = 20
        self.rect.y = DISP_HEI - 114
        self.vel_x = 15.0
        self.vel_y = 0.0
        self.grav = 8

        self.score = 0
        self.runed = 0
        self.lifes = 2
        self.pause = False

        self.anim = 0

        self.item_chance = 0.04

        self.state = 'stand'
        self.former = 'stand'

        self.power = {
            'fly': 0
        }

        self.save = {
            'punctuations': [],
            'unloked': []
        }

        self.world = WorlTest()

    def update(self):
        if self.state == 'jump':
            self.rect.y = self.rect.y - self.vel_y
            self.vel_y = self.vel_y - self.grav
            if self.vel_y < 0 and self.rect.y >= DISP_HEI - 114:
                self.vel_y = 0
                self.rect.y = DISP_HEI - 114
                self.state = 'run'

        if player.world.obstacles:
            for obstacle in player.world.obstacles:
                if self.rect.colliderect(obstacle.rect):
                    obstacle.collision()

        if self.state != 'stand' and self.state != 'dead':
            self.runed += self.vel_x/100.0

    def draw(self):
        if len(self.images[self.state]):
            self.anim += 1
            if self.anim >= len(self.images[self.state]):
                self.anim = 0
        game.blit(self.images[self.state][self.anim], (self.rect.x, self.rect.y))

    def close(self):
        """It should save punctuations to a save file"""
        pass  # need to implement

    def logger(self):
        print(f"player.rect.x {self.rect.x}\nplayer.rect.y {self.rect.y}\nplayer.vel_x {self.vel_x}\nplayer.vel_y {self.vel_y}\n")
