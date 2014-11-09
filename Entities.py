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
        self.hitboxWidth = 20
        self.hitboxHeight = 20
        self.color = (30, 30, 100)

        self.flying = True
        self.beingMoved = False
        self.jumpState = 0 #0 : Not jumping 1: Jumped 2: DoubledJumped

        self.jumpVelocity = 7
        self.maxSpeed = 8
    def move(self):
        if(self.x + self.vx + self.hitboxWidth < self.arcade.GAME_WIDTH and self.vx > 0 or self.x + self.vx > 0 and self.vx < 0):
            if(not self.beingMoved): # slow down if not actively moving
                self.vx = (self.vx * (1-AIR_DRAG))
            self.x = int(self.x + self.vx)
        else: # boundary
            self.vx = 0
        if(self.y + self.vy + self.hitboxHeight < self.arcade.GAME_HEIGHT and self.vy > 0 or self.y + self.vy > 0 and self.vy < 0):
            self.y = int(self.y + self.vy)
            #self.vy = (self.vy * (1-AIR_DRAG))
        else:
            self.vy = 0

        #set flying flag
        #self.flying = True if self.vy is not 0 else False
        #TODO: TEMP:
        if(self.y > self.arcade.GAME_HEIGHT - self.hitboxHeight - 10):
            self.jumpState = 0

        #round speeds if too low
        if abs(self.vx) < 0.05:
            self.vx = 0
        if abs(self.vy) < 0.05:
            self.vy = 0

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
    def logic(self):
        if(self.flying):
            self.changeVy(0.4)
        self.move()
    def draw(self):
        self.arcade.root.fill(self.color, (self.x, self.y, self.hitboxWidth, self.hitboxHeight))

class Player(Entity):
    def __init__(self, arcade):
        Entity.__init__(self, arcade)
