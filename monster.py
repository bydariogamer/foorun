# system modules
import pygame
import random
import sys
# local modules
from monster import *
from item import *
from background import *
from world import *
from animation import *
from constants import *
from player import *


class Monster(object):
    """This is a generic class for monster sprites"""

    def __init__(self):
        super().__init__()
        self.name = 'generic_monster'
        self.image = pygame.image.load('assets/images/monster/test/monster.png')
        self.rect = self.image.get_rect()
        self.rect.x = DISP_WID + random.randint(300, 500)
        self.rect.y = DISP_HEI - 114
        self.sound = pygame.mixer.Sound('assets/sounds/hurt.wav')
        self.collided = False
        player.score += 1

    def update(self):
        self.rect.x -= player.vel_x

    def draw(self):
        game.blit(self.image, (self.rect.x, self.rect.y))

    def collision(self):
        if not self.collided:
            player.lifes -= 1
            self.sound.play()
            self.collided = True


class MonsterTest(Monster):
    """generic monster class for testing"""
    def __init__(self):
        super().__init__()


class Cactus(Monster):
    def __init__(self):
        super().__init__()
        self.name = 'cactus'
        self.image = pygame.image.load('assets/images/monster/cactus.png')
        self.image.set_colorkey((0, 0, 0))


class Dino(Monster):
    def __init__(self):
        super().__init__()
        self.name = 'dino'
        self.image = pygame.image.load('assets/images/monster/dino.png')
        self.image.set_colorkey((0, 0, 0))


class Spike(Monster):
    def __init__(self):
        super().__init__()
        self.name = 'spike'
        self.image = pygame.image.load('assets/images/monster/spike.png')
        self.image.set_colorkey((0, 0, 0))


class Plane(Monster):
    def __init__(self):
        super().__init__()
        self.name = 'plane'
        self.image = pygame.image.load('assets/images/monster/plane.png')
        self.image.set_colorkey((0, 0, 0))
        self.rect.y = DISP_HEI - random.choice((50, 120))