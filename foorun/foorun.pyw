#import modules
import pygame
import random

#initialize pygame
pygame.init()

#set window mesures, title, icon
disp_wid=800
disp_hei=400
disp_tit='foorun'
disp_ico=pygame.image.load('res/man2.png')
clock=pygame.time.Clock()

#initialize window
pygame.display.set_caption(disp_tit)
pygame.display.set_icon(disp_ico)
game = pygame.display.set_mode((disp_wid,disp_hei))

#constants
BLACK=(0,0,0)
WHITE=(255,255,255)
GRAV=4

#images
man=(pygame.image.load('res/man0.png'),pygame.image.load('res/man1.png'),pygame.image.load('res/man2.png'),pygame.image.load('res/man3.png'))
spike=pygame.image.load('res/spike.png')
cactus=pygame.image.load('res/cactus.png')
dino=pygame.image.load('res/dino.png')

#definde game variables
close=False            #if user wants to close
alive=True             #if you smashes your face or not
obstc=[]               #list of obstacles
chary=0                #the position of man to floor
runin=0                #game started and animation
anim_run=[1, 2, 3, 2,] #makes the animation ping-pong
jump=False             #if man is jumping
speed=0                #the man speed

#define functions
#this function might work on the future for screen blink
"""
def invertImg(img):
    #Inverts the colors of a pygame Screen

    img.lock()

    for x in range(img.get_width()):
        for y in range(img.get_height()):
            RGBA = img.get_at((x,y))
            for i in range(3):
                # Invert RGB, but not Alpha
                RGBA[i] = 255 - RGBA[i]
            img.set_at((x,y),RGBA)

    img.unlock()
"""

while not close:
    #event update
    for event in pygame.event.get():
        
        #if spacebar is pressed
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            if not runin:
                runin = 1 #start the game
            if chary==0:
                speed = 30#jump
                jump = True
        #if user wants to exit        
        if event.type==pygame.QUIT:
            close=True    #breaks the while loop

    #game logic
    if jump:
        chary=chary-speed
        speed=speed-GRAV
        if speed== -30:
            speed=0
            chary=0
            jump=False
    #draw window
    game.fill(WHITE)
    pygame.draw.line(game, BLACK, (0,350), (800,350))
    if runin:
        game.blit(man[anim_run[runin-1]],(50,286+chary))
        runin += 1
        runin %= 4
        runin += 1
    else:
        game.blit(man[0],(50,286))

    #update window
    pygame.display.update()
    clock.tick(34)
    
#if the game finish, we just close everything:
pygame.quit()
print('bye')
exit()
