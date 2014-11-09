import random

MAP_WIDTH = 10
MAP_HEIGHT = 10
class Map:
    def __init__(self, arcade):
        self.arcade = arcade
        self.mapArray = []
        self.entities = []

        for y in range(0, MAP_HEIGHT):
            self.mapArray.append([])
            for x in range(0, MAP_WIDTH):
                self.mapArray[y].append(MapSegment(self.arcade))

        self.mapArray[0][0].addObject(MapObject(self.arcade))
        width = 30
        height = 10
        for i in range(0, 10):
            currentObject = SolidObject(self.arcade)
            currentObject.x = random.randint(0, self.arcade.GAME_WIDTH - width)
            currentObject.y = random.randint(0, self.arcade.GAME_HEIGHT - height)
            self.mapArray[0][0].addObject(currentObject)
    def draw(self):
        y = 0
        x = 0
        self.mapArray[y][x].draw()
        for entity in self.entities:
            entity.draw()
            self.arcade.root.fill((20, 20, 20), (entity.x, entity.y, 5, 5))
            self.arcade.root.fill((20, 20, 20), (entity.x + entity.getWidth(), entity.y, 5, 5))
            self.arcade.root.fill((20, 20, 20), (entity.x + entity.getWidth(), entity.y + entity.getHeight(), 5, 5))
            self.arcade.root.fill((20, 20, 20), (entity.x, entity.y + entity.getHeight(), 5, 5))
    def logic(self):
        for entity in self.entities:
            entity.logic()
        for y in range(0, len(self.mapArray)):
            for x in range(0, len(self.mapArray[y])):
                currentSegment = self.mapArray[y][x]
                currentSegment.logic()

    def _getCurrentMapSegments(self, x, y):
        pass


class MapSegment:
    def __init__(self, arcade):
        self.arcade = arcade
        self.entities = []
        self.objectContainer = []
    def draw(self):
        for object in self.objectContainer:
            object.draw()
    def addObject(self, object):
        self.objectContainer.append(object)
    def addEntity(self, entity):
        self.entities.append(entity)
        self.arcade.map.entities.append(entity)
    def removeEntity(self, entity):
        if entity in self.entity:
            self.entities.remove(entity)
        if entity in self.arcade.map.entities:
            self.arcade.map.entities.remove(entity)
    def logic(self):
        self.checkForCollisions()
    def checkForCollisions(self):
        #between entities
        collisionType = 0 #0 means none, 1 means TL, 2 means TR, 3 means BL, 4 means BR
        for entity in self.entities:
            for collider in self.entities:
                pass
                #TODO: Make entity collisions
                ##top left
                #if entity.x > collider.x and entity.x < collider.x + collider.getWidth():
                    #if entity.y > collider.y and entity.y < collider.y + collider.getHeight():
                        #print("Top left collision between " + str(entity) + " and " + str(collider))
        for entity in self.entities:
            for collider in self.objectContainer:
                collisionType = 0
                #top left
                if entity.x > collider.x and entity.x < collider.x + collider.getWidth():
                    if entity.y > collider.y and entity.y < collider.y + collider.getHeight():
                        collisionType = 1
                #top right
                if entity.x + entity.getWidth() > collider.x and entity.x + entity.getWidth() < collider.x + collider.getWidth():
                    if entity.y > collider.y and entity.y < collider.y + collider.getHeight():
                        collisionType = 2
                #bottom left
                if entity.x > collider.x and entity.x < collider.x + collider.getWidth():
                    if entity.y + entity.getHeight() > collider.y and entity.y + entity.getHeight() < collider.y + collider.getHeight():
                        collisionType = 3
                #bottom right
                if entity.x + entity.getWidth() > collider.x and entity.x + entity.getWidth() < collider.x + collider.getWidth():
                    if entity.y + entity.getHeight() > collider.y and entity.y + entity.getHeight() < collider.y + collider.getHeight():
                        collisionType = 4
                collisionString = ["None","Top left","Top right","Bottom left","Bottom right"][collisionType]
                if collisionType is not 0:
                    #print(collisionString + " collision between entity and object:  " + str(entity) + " and " + str(collider))
                    entity.collision(collider, collisionType)
                    collider.collision(entity, collisionType)

class MapObject:
    def __init__(self, arcade):
        self.arcade = arcade
        self.x = 100
        self.y = 100
        self.width = 100
        self.height = 20
        self.texture = None
        self.visible = True
        self.color = (200, 200, 200)

    def draw(self):
        self.arcade.root.fill(self.color, (self.x, self.y, self.width, self.height))
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
    def collision(self, collider, collisionType):
        pass

class SolidObject(MapObject):
    def __init__(self, arcade):
        MapObject.__init__(self, arcade)
        self.color = (100, 255, 0)
