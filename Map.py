
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
    def draw(self):
        y = 0
        x = 0
        self.mapArray[y][x].draw()
        for entity in self.entities:
            entity.draw()
    def logic(self):
        for entity in self.entities:
            entity.logic()

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

class MapObject:
    def __init__(self, arcade):
        self.arcade = arcade
        self.x = 100
        self.y = 100
        self.width = 20
        self.height = 20
        self.texture = None
        self.visible = True

    def draw(self):
        self.arcade.root.fill((100, 100, 0), (self.x, self.y, self.width, self.height))
