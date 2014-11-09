#!/usr/bin/python

import pygame
from pygame import *
from pygame.locals import *
from Map import Map
from Entities import *

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

GAME_WIDTH = 600
GAME_HEIGHT = 500

class Arcade:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.frame = 0
        self.logicFrame = 0
        self.mouseX = 0
        self.mouseY = 0
        self.running = True
        self.map = Map(self)
        self.heldKeys = dict()
        self.root = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT), pygame.DOUBLEBUF)

        self.player = Player(self)
        while self.running:
            self.displayLoop()
        self.quit()
    def quit(self):
        print("Exiting game")
    def displayLoop(self):
        self.root.fill((100,0,0))
        self.clock.tick(LOGIC_PER_SEC)
        self.logicFrame += 1
        if(self.logicFrame % 2 is 0):
            self.frame += 1
            self.drawMap()
            self.drawUI()
            #force call mouse move to redraw mouse
            self.handleMouseMove()
            self.eventLoop()
            self.handleKeyHold()
            pygame.display.flip() #used in pygame
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
        if(x + textSurface.get_width() > GAME_WIDTH):
            x = GAME_WIDTH - textSurface.get_width() 
        if(y + textSurface.get_height() > GAME_HEIGHT):
            y = GAME_HEIGHT - textSurface.get_height() 
        pos = (x, y)
        if(background is not None):
            self.root.fill(background, (pos[0], pos[1], textSurface.get_width(), textSurface.get_height()))
        self.root.blit(textSurface, (pos[0], pos[1], textSurface.get_width(), textSurface.get_height()))
    def drawUI(self):
        self.drawText("Frame: " + str(self.frame), (0, 0))
        self.drawText("Logic frame: " + str(self.logicFrame), (0, 15))
    def handleMouseMove(self):
        mouseX = self.mouseX
        mouseY = self.mouseY
        self.drawText("X:"+str(mouseX)+" Y:"+str(mouseY), (self.mouseX + 10, self.mouseY + 10))
    def handleMouseClick(self, event):
        pass 
    def handleMouseRelease(self, event):
        pass
    def handleKeyHold(self):
        self.drawText(self.heldKeys, (GAME_WIDTH, 0))
    def handleKeyDown(self, event):
        self.heldKeys.update({event.key:event.mod})
    def handleKeyRelease(self, event):
        #print(event)
        del self.heldKeys[event.key]
        if event.key == K_ESCAPE:
            self.running = False
    def version(self):
        print(pygame.get_sdl_version())



if __name__ == "__main__":
    Arcade()
