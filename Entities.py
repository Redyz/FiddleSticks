import pygame
from pygame import *

GRAVITATIONAL_CONSTANT = 9.8
MAX_HORIZONTAL_SPEED = 10 #TODO: Probably unused
MAX_VERTICAL_SPEED = 30
AIR_DRAG = 0.1 # in percent 

class Entity:
    def __init__(self, arcade):
        self.arcade = arcade
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.color = (70, 70, 100)

        self.hitbox = pygame.Surface((100, 100))
        self.hitbox.set_colorkey((0,0,0)) #black is transparent
        pygame.draw.polygon(self.hitbox, self.color, [(10,0), (50,0), (60, 40), (20, 50), (5,45)])

        #fit surface to drawn size
        size = self.hitbox.get_bounding_rect()
        chopped = self.hitbox.copy()
        self.hitbox = Surface((size.width, size.height))
        self.hitbox.set_colorkey(chopped.get_colorkey())
        self.hitbox.blit(chopped, (0,0), size)

        self.flying = True
        self.beingMoved = False
        self.supported = False
        self.jumpState = 0 #0 : Not jumping 1: Jumped 2: DoubledJumped

        self.jumpVelocity = 7
        self.maxSpeed = 8
    def move(self):
        if(self.x + self.vx + self.hitbox.get_width() < self.arcade.GAME_WIDTH and self.vx > 0 or self.x + self.vx > 0 and self.vx < 0):
            if(not self.beingMoved): # slow down if not actively moving
                self.vx = (self.vx * (1-AIR_DRAG))
            self.x = int(self.x + self.vx)
        else: 
            self.vx = 0
        if(self.y + self.vy + self.hitbox.get_height() < self.arcade.GAME_HEIGHT and self.vy > 0 or self.y + self.vy > 0 and self.vy <= 0):
            self.y = int(self.y + self.vy)
            print(self.vy)
            if(not self.supported and abs(self.vy) < 0.05):
                self.flying = True
                print("dropped")
                self.vy = 0.5
            if(self.vy > 0):
                self.vy = (self.vy * 1.005)
        else:
            self.vy = 0

        #set flying flag
        #self.flying = True if self.vy is not 0 else False
        #TODO: TEMP:
        if(self.y > self.arcade.GAME_HEIGHT - self.hitbox.get_height() - 10):
            self.jumpState = 0

        #round speeds if too low
        if abs(self.vx) < 0.05:
            self.vx = 0
        if abs(self.vy) < 0.05:
            self.vy = 0

        self.supported = False
        self.beingMoved = False
    def changeVx(self, vx):
        if abs(self.vx + vx) < self.maxSpeed:
            self.vx += vx
    def changeVy(self, vy):
        self.vy += vy
    def setVx(self, vx):
        self.vx = vx
    def setVy(self, vy):
        self.vy = vy
    def jump(self):
        self.changeVy(-self.jumpVelocity)
        self.flying = True
    def logic(self):
        if(self.flying):
            self.changeVy(0.4)
        self.move()
    def getWidth(self):
        return self.hitbox.get_width()
    def getHeight(self):
        return self.hitbox.get_height()
    def draw(self):
        self.arcade.root.blit(self.hitbox, (self.x, self.y))
    def collision(self, collider, collisionType):
        #Bottom collision
        if collisionType == 3 or collisionType == 4:
            self.vy = 0
            self.y = collider.y - self.getHeight() + 1
            self.flying = False
            self.supported = True
            self.jumpState = 0
        #Top collision
        #if collisionType == 1 or collisionType == 2:
            #self.vx = 0

class Player(Entity):
    def __init__(self, arcade):
        Entity.__init__(self, arcade)
