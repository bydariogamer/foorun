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


class Item(object):

    def __init__(self):
        super().__init__()
        self.name = 'generic_item'
        self.image = pygame.image.load('assets/images/item/test/item.png')
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = DISP_WID + random.randint(300, 500)
        self.rect.y = DISP_HEI - 114
        self.sound = pygame.mixer.Sound('assets/sounds/lifeup.wav')
        self.collided = False

    def update(self):
        self.rect.x -= player.vel_x

    def draw(self):
        game.blit(self.image, (self.rect.x, self.rect.y))

    def collision(self):
        if not self.collided:
            player.lifes += 1
            self.sound.play()
            self.collided = True


class ItemTest(Item):
    """generic item class for testing"""
    def __init__(self):
        super().__init__()


class Life(Item):
    """this item gives a life to player"""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/images/item/life.png')
        self.image.set_colorkey((0, 0, 0))


class Coin(Item):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/images/item/coin.png')
        self.image.set_colorkey((0, 0, 0))
        self.sound = pygame.mixer.Sound('assets/sounds/coin.mp3')

    def collision(self):
        if not self.collided:
            player.score += 10
            self.sound.play()
            self.collided = True
			