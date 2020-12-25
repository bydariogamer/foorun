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

#---initialize window
pygame.display.set_caption(disp_tit)
pygame.display.set_icon(disp_ico)
game = pygame.display.set_mode((disp_wid,disp_hei))

#---constants
BLACK =(0,0,0)
WHITE =(255,255,255)
GRAV = 4 #maybe the man gets to the moon running... what if i change it?
FONT = pygame.font.Font("res/8bitOperatorPlus-Bold.ttf", 32)

#---images
#runner
man=[
    pygame.image.load('res/man0.png'),
    pygame.image.load('res/man1.png'),
    pygame.image.load('res/man2.png'),
    pygame.image.load('res/man3.png')
    ]
for img in man:
    img.set_colorkey(WHITE)
#---obstacles

    
#---definde game variables

close = False             #if user wants to close
alive = True              #if the player is alive
obstacles = []            #list of obstacles
chary = 0                 #the position of man to floor
runin = 0                 #game started and animation
anim_run = [1, 2, 3, 2,]  #makes the animation ping-pong
jump = False              #if man is jumping
vel_y = 0                 #the man speed in Y
vel_x = 20                #the man speed in X

#define classes
class Obstacle():
    
    obst_dict = {
        'dino':pygame.image.load('res/dino.png'),
        'cactus':pygame.image.load('res/cactus.png'),
        'spike':pygame.image.load('res/spike.png'),
        'plane':pygame.image.load('res/plane.png')
        }
    for name in obst_dict:
        obst_dict[name].set_colorkey(WHITE)
        
    def __init__(self):
        
        #distance
        if not obstacles:
            self.distance = disp_wid + random.randint(100,200)
        else:
            self.distance = obstacles[len(obstacles)-1].distance + random.randint(10*vel_x,30*vel_x)
            
        #name
        self.name = random.choice(list(self.obst_dict.keys()))
        
        #high
        if self.name == 'plane' : #self.high = random.randint(0, 1) if name == 'plane' else 0
            self.high=random.randint(0,1)
        else:
            self.high=0
            
        #image
        self.image=self.obst_dict[self.name]
        
        self.alive=True #delete this! put it in class Player()

    def update(self):
        ob.distance -= vel_x
            
    def draw(self):
        if self.distance < disp_wid:
            if self.high:
                game.blit(self.image, (114+self.distance , 222))
            else:
                game.blit(self.image, (114+self.distance , 286))
                
    def colision(self):
        if self.distance > -64 and self.distance < -32:
            if self.high:
                if chary < -70 and chary > -120:
                    self.alive = False

            else:
                if chary > -64:
                    self.alive = False

                    
class Player():

    def __init__(self):
        self.y=0
        self.lifes=1
        self.vel_x=0
        self.vel_y=0
        self.jump=False
        self.alive=True
        self.runin=0
        self.image=man[0]
        self.grav=4
        self.score=0

    def update(self):
        if self.alive:
            if self.jump: 
                chary = chary - vel_y
                vel_y = vel_y - GRAV
                if vel_y== -30:
                    vel_y=0
                    chary=0
                    jump=False

        
    def draw(self):
        pass #memento: implement a draw methode

class Tool():
    
    def __init__(self):
        self.lifes=0
        self.vel_x=0
        self.grav=0



        
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
            close = True  #breaks the while loop

    #game logic
    if alive:
                    
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
        for obs in obstacles:
            if obs is not None:
                obs.draw()
                obs.colision()
            

        for obs in obstacles:
            if obs is not None:
                if not obs.alive:
                    alive = False
                if obs.distance < -200:
                    obs = None    
    else: #if not alive
        if obstacles:
            score=len(obstacles)
        obstacles.clear()
        game.fill(BLACK)
        game.blit(FONT.render("YOU LOSE",True,WHITE),(50,50))
        game.blit(FONT.render("YOUR SCORE IS:",True,WHITE),(50,100))
        game.blit(FONT.render(str(score),True,WHITE),(50,150))
        game.blit(FONT.render("PRESS SPACEBAR TO RETRY",True,WHITE),(50,200))

    #update window
    pygame.display.update()
    clock.tick(34)
        
                    
    #if the game finish, we just close everything:
pygame.quit()
print('bye')
exit()
