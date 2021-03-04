# import modules
import pygame
import random
import sys
# import math

# todo add music
# todo add characters
# todo change speed with distance

"""this game is an infinite-running where you have to avoid
smashing your sweet face against absurd obstacles"""

# initialize pygame
pygame.init()
pygame.mixer.init()

# set window mesures, title, icon
DISP_WID = 800
DISP_HEI = 400
DISP_TIT = 'FOORUN'
DISP_ICO = pygame.image.load('assets/images/icon/icon.png')
clock = pygame.time.Clock()

# ---initialize window
pygame.display.set_caption(DISP_TIT)
pygame.display.set_icon(DISP_ICO)
game = pygame.display.set_mode((DISP_WID, DISP_HEI))

# ---constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FONT = pygame.font.Font("assets/fonts/8bitOperatorPlus-Bold.ttf", 32)
LIFE = pygame.image.load("assets/images/icon/life.png")
LIFE.set_colorkey(WHITE)
LIFE.convert()


# ---define classes
# class Animation
class Animation(object):
    def __init__(self, *args: pygame.Surface, pingpong=False):
        """takes any number of Surface objects to make an Animation object"""
        for arg in args:
            if not isinstance(arg, pygame.Surface):
                raise TypeError("All arguments must be surfaces")
        self.surfaces = list(args)
        self.pingpong = pingpong
        self._i = 0

    def __iter__(self):
        return iter(self.surfaces)

    def draw(self, image=None):
        """return the next Surface each time"""
        if image is None:
            self._i += 1
            if not self.pingpong:
                self._i %= len(self.surfaces)
            else:
                self._i %= len(self.surfaces) * 2
            if self._i < len(self.surfaces):
                return self.surfaces[self._i]
            else:
                return self.surfaces[len(self.surfaces) * 2 - self._i]
        else:
            return self.surfaces[image]

    def crazy(self):
        return random.choice(self.surfaces)


# class Player
class Player(pygame.sprite.Sprite):
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
                image.set_colorkey(WHITE)
                image.convert()

        self.rect = self.images['run'][0].get_rect()

        self.rect.x = 50
        self.rect.y = DISP_HEI - 114
        self.vel_x = 20.0
        self.vel_y = 0.0
        self.grav = 3.5

        self.score = 0
        self.runed = 0
        self.lifes = 3
        self.pause = False

        self.anim = 0

        self.item_chance = 0.1

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
            if self.vel_y < 0 and self.rect.y <= DISP_HEI - 114:
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
        pass  # need to implement


# class Monster
class Monster(pygame.sprite.Sprite):
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
        self.image.set_colorkey(WHITE)


class Dino(Monster):
    def __init__(self):
        super().__init__()
        self.name = 'dino'
        self.image = pygame.image.load('assets/images/monster/dino.png')
        self.image.set_colorkey(WHITE)


class Spike(Monster):
    def __init__(self):
        super().__init__()
        self.name = 'spike'
        self.image = pygame.image.load('assets/images/monster/spike.png')
        self.image.set_colorkey(WHITE)


class Plane(Monster):
    def __init__(self):
        super().__init__()
        self.name = 'plane'
        self.image = pygame.image.load('assets/images/monster/plane.png')
        self.image.set_colorkey(WHITE)
        self.rect.y = DISP_HEI - random.choice((50, 120))


# class Item
class Item(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.name = 'generic_item'
        self.image = pygame.image.load('assets/images/item/test/item.png')
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = DISP_WID + random.randint(15*vel_x,30*vel_x)
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
        self.image.set_colorkey(WHITE)


class Coin(Item):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/images/item/coin.png')
        self.image.set_colorkey(WHITE)
        self.sound = pygame.mixer.Sound('assets/sounds/coin.mp3')

    def collision(self):
        if not self.collided:
            player.score += 10
            self.sound.play()
            self.collided = True


# class Background
class Background(object):
    def __init__(self, image: pygame.Surface or str):
        """pass a surface to create a new background"""
        if type(image) == pygame.Surface:
            self.image = image
        elif type(image) == str:
            self.image = pygame.image.load(image)
        else:
            raise TypeError(
                f"argument must be a Surface or a String with a path to an image, but {str(type(image))} was given")
        self.width = self.image.get_width()
        self.camera = pygame.Rect((0, 0), (DISP_WID, DISP_HEI))
        self.gamearea = pygame.Surface((DISP_WID, DISP_HEI))
        self.color = pygame.transform.average_color(self.image, self.image.get_rect())

    def draw(self, pause=False):
        if not pause:
            self.camera.left += player.vel_x / 5
        if self.camera.right >= self.width:
            self.camera.left = 0
        self.gamearea.blit(self.image, (0, 0), self.camera)
        return self.gamearea


class BackgroundTest(Background):
    def __init__(self):
        super().__init__(pygame.image.load('assets/images/background/test/background.png'))


# class World
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
                    random.choice(self.item_list)

            elif not self.obstacles:
                if random.random() > player.item_chance:
                    self.obstacles.append(random.choice(self.monster_list)())
                else:
                    random.choice(self.item_list)
        if self.obstacles:
            for obstacle in self.obstacles:
                if obstacle is not None:
                    obstacle.update()
                # why is this not working as it should?
##                if obstacle.rect.x < -64:
##                    obstacle = None
##                    player.score += 1
        if player.lifes <= 0:
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
            player.vel_y += 40.0
            player.state = 'jump'


class WorlTest(World):
    def __init__(self):
        super().__init__()


class Ender(World):
    def __init__(self):
        super().__init__()

    @staticmethod
    def update():
        pass

    @staticmethod
    def draw():
        game.fill(BLACK)
        game.blit(FONT.render("YOU LOSE", True, WHITE), (50, 40))
        game.blit(FONT.render("YOUR SCORE IS:", True, WHITE), (50, 110))
        game.blit(FONT.render(str(player.score), True, WHITE), (50, 155))
        game.blit(FONT.render("YOUR DISTANCE IS:", True, WHITE), (50, 235))
        game.blit(FONT.render(str(int(player.runed)), True, WHITE), (50, 280))
        game.blit(FONT.render("PRESS SPACEBAR TO RETRY", True, WHITE), (50, 350))

    @staticmethod
    def spacebar():
        player.rect.x = 50
        player.rect.y = DISP_HEI - 114
        player.vel_x = 20.0
        player.vel_y = 0.0
        player.grav = 3.5
        player.score = 0
        player.runed = 0
        player.lifes = 3
        player.pause = False
        player.anim = 0
        player.item_chance = 0.1
        player.state = 'stand'
        player.power = {'fly': 0}
        player.world = WorlTest()


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
    dt = clock.tick(34)  # like this or like:` clock.tick(60); dt = clock.tick() ` ?

# game end routine
# player.save()
pygame.quit()
print('bye')
sys.exit()
