
MAP_WIDTH = 10
MAP_HEIGHT = 10
class Map:
    def __init__(self, arcade):
        self.arcade = arcade
        self.mapArray = []
        for y in range(0, MAP_HEIGHT):
            self.mapArray.append([])
            for x in range(0, MAP_WIDTH):
                self.mapArray[y].append(MapSegment(self.arcade))

        self.mapArray[0][0].addObject(MapObject(self.arcade))
    def draw(self):
        y = 0
        x = 0
        self.mapArray[y][x].draw()
    def _getCurrentMapSegments(self, x, y):
        pass


class MapSegment:
    def __init__(self, arcade):
        self.arcade = arcade
        self.objectContainer = []
    def draw(self):
        for object in self.objectContainer:
            object.draw()
    def addObject(self, object):
        self.objectContainer.append(object)

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
