
class Entity:
    def __init__(self, arcade):
        self.arcade = arcade
        self.x = 0
        self.y = 0

class Player(Entity):
    def __init__(self, arcade):
        Entity.__init__(self, arcade)
