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
BLACK =(0,0,0)
WHITE =(255,255,255)
GRAV = 4 #maybe the man gets to the moon running... what if i change it?
FONT = pygame.font.Font("res/8bitOperatorPlus-Bold.ttf", 32)

#images
man0=pygame.image.load('res/man0.png')
man0.set_colorkey(WHITE)
man1=pygame.image.load('res/man1.png')
man1.set_colorkey(WHITE)
man2=pygame.image.load('res/man2.png')
man2.set_colorkey(WHITE)
man3=pygame.image.load('res/man3.png')
man3.set_colorkey(WHITE)
spike=pygame.image.load('res/spike.png')
spike.set_colorkey(WHITE)
cactus=pygame.image.load('res/cactus.png')
cactus.set_colorkey(WHITE)
dino=pygame.image.load('res/dino.png')
dino.set_colorkey(WHITE)
plane=pygame.image.load('res/plane.png')
plane.set_colorkey(WHITE)

#definde game variables
man=(man0,man1,man2,man3)#tuple with all the man frames
close=False             #if user wants to close
alive=True              #if you smashes your face or not
obstacles=[]            #list of obstacles
chary=0                 #the position of man to floor
runin=0                 #game started and animation
anim_run=[1, 2, 3, 2,]  #makes the animation ping-pong
jump=False              #if man is jumping
vel_y=0                 #the man speed in Y
vel_x=10                #the man speed in X
obst_names=('dino','cactus','spike','plane')
obst_images={
    'dino':dino,
    'cactus':cactus,
    'spike':spike,
    'plane':plane
    }

#define functions


#define classes
class Obstacle():
    def __init__(self):
        if not obstacles:
            self.distance = disp_wid + random.randint(100,400)
        else:
            self.distance = obstacles[len(obstacles)-1].distance + random.randint(100,400)
        self.name = random.choice(obst_names)
        if self.name == 'plane' : #self.high = random.randint(0, 1) if name == 'plane' else 0
            self.high=random.randint(0,1)
        else:
            self.high=0
        self.image=obst_images[self.name]
    def draw(self):
        if self.distance < disp_wid:
            if self.high:
                game.blit(self.image, (114+self.distance , 222))
            else:
                game.blit(self.image, (114+self.distance , 286))
    def colision(self):
        if self.distance > 0 and self.distance < 64:
            if self.high:
                if chary > 70 and chary < 130:
                    alive=False
            else:
                if chary < 70:
                    alive=False
while not close:
    #event update
    for event in pygame.event.get():
        
        #if spacebar is pressed
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            if not runin:
                runin = 1 #start the game
            if chary==0:
                vel_y = 30#jump
                jump = True
            if not alive:
                alive = True
        #if user wants to exit        
        if event.type==pygame.QUIT:
            close=True    #breaks the while loop

    #game logic
    if jump:
        chary=chary-vel_y
        vel_y=vel_y-GRAV
        if vel_y== -30:
            vel_y=0
            chary=0
            jump=False
    for ob in obstacles:
        if ob is not None:
            ob.distance -= vel_x
        
    #draw window
    game.fill(WHITE)
    pygame.draw.line(game, BLACK, (0,350), (800,350))
    
    if alive:
        if runin: #draw the man running
            game.blit(man[anim_run[runin-1]],(50,286+chary))
            runin += 1
            runin %= 4
            runin += 1
            if not obstacles:
                obstacles.append(Obstacle())
            if obstacles:
                if obstacles[len(obstacles)-1].distance < disp_wid:
                    obstacles.append(Obstacle())
        else:     #draw the man standing
            game.blit(man[0],(50,286))
        game.blit(FONT.render(str(len(obstacles)),True,BLACK),(50,50))    
        for i in range(len(obstacles)):
            if obstacles[i] is not None:
                obstacles[i].draw()
                obstacles[i].colision()
        
        #update window
        pygame.display.update()
        clock.tick(34)
        
    if not alive:
        game.fill(BLACK)
        ender = FONT.render("YOU LOSE\nYOUR SCORE IS "+str(len(obstacles))+"\nPRESS SPACEBAR TO RETRY", True, WHITE)
        game.blit(ender,(50,50))
    for i in range(len(obstacles)):
        if obstacles[i] is not None:
            if obstacles[i].distance < -200:
                obstacles[i] = None
#if the game finish, we just close everything:
pygame.quit()
print('bye')
exit()
