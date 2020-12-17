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
pygame.display.set_caption('VERASAUR')
pygame.display.set_icon(disp_ico)
game = pygame.display.set_mode((disp_wid,disp_hei))

#constants
BLACK=(0,0,0)
WHITE=(255,255,255)

#definde game variables
close=False
alive=True
obstc=[]
chary=0
runin=0
man=(pygame.image.load('res/man0.png'),pygame.image.load('res/man1.png'),pygame.image.load('res/man2.png'),pygame.image.load('res/man3.png'))
spike=pygame.image.load('res/spike.png')
speed=0

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
    game.fill(WHITE)
    pygame.draw.line(game, BLACK, (0,350), (800,350))
    if runin:
        if runin==1:
            game.blit(man[1],(50,286+chary))
            runin=2
        if runin==2:
            game.blit(man[2],(50,286+chary))
            runin=3
        if runin==3:
            game.blit(man[3],(50,286+chary))
            runin=4
        if runin==4:
            game.blit(man[2],(50,286+chary))
            runin=1
    else:
        game.blit(man[0],(50,286))
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            if not runin:
                runin = 1
            if chary==0:
                speed = 20
                
        if event.type==pygame.QUIT:
            close=True
    pygame.display.update()
    clock.tick(60)
    
#if the game finish, we just close everything:
pygame.quit()
print('bye')
exit()
