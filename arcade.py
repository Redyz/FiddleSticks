#!/usr/bin/python

import pygame
from pygame import *
from pygame.locals import *
from Map import Map
from Entities import *
from Keys import *

#FONT SETTINGS
pygame.font.init()
uiFont = pygame.font.SysFont("impact",20)
uiTextcolor = (255, 255, 255)

#CONTROLS
LCLICK = 1
MCLICK = 2
RCLICK = 3
FWDM = 4
BWDM = 5

FRAMES_PER_SEC = 60
LOGIC_PER_SEC = 2*FRAMES_PER_SEC


class Arcade:
    def __init__(self):
        #GLOBAL CONSTS
        self.GAME_WIDTH = 600
        self.GAME_HEIGHT = 500

        self.clock = pygame.time.Clock()
        self.frame = 0
        self.logicFrame = 0
        self.mouseX = 0
        self.mouseY = 0
        self.running = True
        self.map = Map(self)
        self.heldKeys = dict()
        self.checkedKeys = dict()

        self.root = pygame.display.set_mode((self.GAME_WIDTH, self.GAME_HEIGHT), pygame.DOUBLEBUF)
        self.player = Player(self)
        self._keySetup()
        #temp
        self.map.mapArray[0][0].addEntity(self.player)
        self.player.x = 100
        self.player.y = 100
        while self.running:
            self.displayLoop()
        self.quit()
    def quit(self):
        print("Exiting game")
    def _keySetup(self):
        spaceKey = Key(self)
        def spaceAction():
            if self.player.jumpState < 2:
                self.player.jump()
                self.player.jumpState += 1
        spaceKey.action = spaceAction
        self.checkedKeys.update({K_SPACE:spaceKey})
    def displayLoop(self):
        self.root.fill((100,100,100))
        self.clock.tick(LOGIC_PER_SEC)
        self.logicFrame += 1
        if(self.logicFrame % 2 is 0):
            self.frame += 1
            self.mapLogic()
            self.drawMap()
            self.drawUI()
            #force call mouse move to redraw mouse
            self.handleMouseMove()
            self.handleKeyHold()
            self.eventLoop()
            pygame.display.flip() #used in pygame
    def mapLogic(self):
        self.map.logic()
    def drawMap(self):
        self.map.draw()
    def eventLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == MOUSEMOTION:
                mouseX, mouseY = event.pos
                self.mouseX = mouseX
                self.mouseY = mouseY
                self.handleMouseMove()
            elif event.type == MOUSEBUTTONUP:
                self.handleMouseClick(event)
            elif event.type == KEYUP:
                self.handleKeyRelease(event)
            elif event.type == KEYDOWN:
                self.handleKeyDown(event)
    def drawText(self, text, pos, background = (40, 40, 40)):
        textSurface = uiFont.render(str(text), 1, uiTextcolor)
        x, y = pos
        if(x + textSurface.get_width() > self.GAME_WIDTH):
            x = self.GAME_WIDTH - textSurface.get_width() 
        if(y + textSurface.get_height() > self.GAME_HEIGHT):
            y = self.GAME_HEIGHT - textSurface.get_height() 
        pos = (x, y)
        if(background is not None):
            self.root.fill(background, (pos[0], pos[1], textSurface.get_width(), textSurface.get_height()))
        self.root.blit(textSurface, (pos[0], pos[1], textSurface.get_width(), textSurface.get_height()))
    def drawUI(self):
        self.drawText("Frame: " + str(self.frame), (0, 0))
        self.drawText("Logic frame: " + str(self.logicFrame), (0, 15))
        self.drawText("P: " + str(self.player.x) + "-" + str(self.player.y) + ", S:" + str(round(self.player.vx, 2)) + "&" + str(round(self.player.vy)), (self.GAME_WIDTH, 15))
        self.drawText("J: " + str(["Idle","Jump","DoubleJumped"][self.player.jumpState]), (self.GAME_WIDTH, 30))
        self.drawText("F: " + str(self.player.flying), (self.GAME_WIDTH, 45))
        self.drawText("S: " + str(self.player.supported), (self.GAME_WIDTH, 60))
        self.drawText(self.heldKeys, (self.GAME_WIDTH, 0))
    def handleMouseMove(self):
        mouseX = self.mouseX
        mouseY = self.mouseY
        self.drawText("X:"+str(mouseX)+" Y:"+str(mouseY), (self.mouseX + 10, self.mouseY + 10))
    def handleMouseClick(self, event):
        pass 
    def handleMouseRelease(self, event):
        pass
    def handleKeyHold(self):
        for key, mod in self.heldKeys.items():
            self.player.beingMoved = True
            if key == K_RIGHT:
                self.player.changeVx(0.5)
            elif key == K_LEFT:
                self.player.changeVx(-0.5)
            currentKey = self.checkedKeys.get(key)
            if currentKey is not None:
                currentKey.logic(self.heldKeys)
    def handleKeyDown(self, event):
        self.heldKeys.update({event.key:event.mod})
    def handleKeyRelease(self, event):
        if(self.heldKeys.get(event.key) is not None):
            del self.heldKeys[event.key]
        if event.key == K_ESCAPE:
            self.running = False
        currentKey = self.checkedKeys.get(event.key)
        if currentKey:
            currentKey.release()
    def version(self):
        print(pygame.get_sdl_version())



if __name__ == "__main__":
    Arcade()
