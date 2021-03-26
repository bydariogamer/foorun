# system modules
import pygame
import random
import sys
# local modules
from monster import *
from item import *
from background import *
from animation import *
from constants import *
from player import *


class World(object):
    def __init__(self):
        self.background = BackgroundTest()
        self.monster_list = [MonsterTest]
        self.item_list = [ItemTest]
        self.obstacles = []
        self.runed = 0

    def update(self):
        player.update()
        if player.state != 'stand':
            if self.obstacles and self.obstacles[len(self.obstacles) - 1].rect.x < DISP_WID:
                if random.random() > player.item_chance:
                    self.obstacles.append(random.choice(self.monster_list)())
                else:
                    self.obstacles.append(random.choice(self.item_list)())

            elif not self.obstacles:
                if random.random() > player.item_chance:
                    self.obstacles.append(random.choice(self.monster_list)())
                else:
                    self.obstacles.append(random.choice(self.item_list)())
        if self.obstacles:
            for obstacle in self.obstacles:
                if obstacle is not None:
                    obstacle.update()

                if obstacle.rect.x < -100:
                    obstacle = None
##                    player.score += 1   # why is this not working as it should?
        if player.lifes < 0:
            player.state = 'dead'
            player.world = Ender()

    def draw(self):
        if player.state == 'stand':
            game.blit(self.background.draw(pause=True), (0, 0))
        else:
            game.blit(self.background.draw(), (0, 0))
        pygame.draw.line(game, BLACK, (0, 350), (800, 350))
        game.blit(FONT.render(str(len(self.obstacles)), True, BLACK), (50, 50))
        game.blit(FONT.render(str(int(player.runed)), True, BLACK), (200, 50))
        game.blit(FONT.render(str(player.lifes), True, BLACK), (500, 50))
        game.blit(LIFE, (550, 50))
        player.draw()
        for obstacle in self.obstacles:
            if obstacle is not None:
                obstacle.draw()
        player.draw()

    @staticmethod
    def spacebar():
        if player.state == 'stand':
            player.state = 'run'

        elif not player.state == 'jump':
            player.vel_y += 50.0
            player.state = 'jump'


class WorlTest(World):
    def __init__(self):
        super().__init__()
    def update(self):
        super().update()
        if TEST:
            player.logger()


class Ender(World):
    def __init__(self):
        super().__init__()

    @staticmethod
    def update():
        pass

    @staticmethod
    def draw():
        game.fill(BLACK)
        game.blit(FONT.render("YOU LOSE", True, WHITE), (50, 30))
        game.blit(FONT.render("YOUR SCORE IS:", True, WHITE), (50, 100))
        game.blit(FONT.render(str(player.score), True, WHITE), (50, 145))
        game.blit(FONT.render("YOUR DISTANCE IS:", True, WHITE), (50, 225))
        game.blit(FONT.render(str(int(player.runed)), True, WHITE), (50, 270))
        game.blit(FONT.render("PRESS SPACEBAR TO RETRY", True, WHITE), (50, 340))

    @staticmethod
    def spacebar():
        player.rect.x = 50
        player.rect.y = DISP_HEI - 114
        player.vel_x = 20.0
        player.vel_y = 0.0
        player.grav = 7
        player.score = 0
        player.runed = 0
        player.lifes = 2
        player.pause = False
        player.anim = 0
        player.item_chance = 0.04
        player.state = 'stand'
        player.power = {'fly': 0}
        player.world = WorlTest()
