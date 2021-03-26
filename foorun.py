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


# todo add music
# todo add characters
# todo change speed with distance

"""this game is an infinite-running where you have to avoid
smashing your sweet face against absurd obstacles"""

# initialize pygame
pygame.init()
pygame.mixer.init()


# ---initialize window
pygame.display.set_caption(DISP_TIT)
pygame.display.set_icon(DISP_ICO)
game = pygame.display.set_mode((DISP_WID, DISP_HEI))
clock = pygame.time.Clock()

# ---constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FONT = pygame.font.Font("assets/fonts/8bitOperatorPlus-Bold.ttf", 32)
LIFE = pygame.image.load("assets/images/icon/life.png")
LIFE.set_colorkey(WHITE)
LIFE.convert()


# create the character:

player = Player()

close = False

# game loop
while not close:

    # ---events
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:  # if any key is pressed
            if event.key == pygame.K_SPACE:  # if spacebar is pressed
                player.world.spacebar()

        if event.type == pygame.QUIT:  # if user wants to exit
            close = True  # breaks the while loop

    # ---logic
    player.world.update()

    # ---render     
    player.world.draw()
    pygame.display.update()  # updates the screen

    # ---tick
    dt = clock.tick(BASE_FPS)  # like this or like:` clock.tick(60); dt = clock.tick() ` ?

# game end routine
# player.save()
pygame.quit()
print('bye')
sys.exit()
