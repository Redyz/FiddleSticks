
class Key:
    def __init__(self, arcade):
        self.arcade = arcade
        self.mod = 0
        self.holdDelay = 10 #in frames
        self._lastTriggered = 0
        self._heldMode = False
    def logic(self, heldKeys):
        if(not self._heldMode):
            self.action()
            self._heldMode = True
        elif(self.arcade.frame - self._lastTriggered > self.holdDelay):
            self.held()
            self._lastTriggered = self.arcade.frame
    def held(self):
        pass
    def action(self):
        pass
    def release(self):
        self._heldMode = False
