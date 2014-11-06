#!/usr/bin/python

import pygame
from pygame import *
from pygame.locals import *

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

class Arcade:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.frame = 0
        self.version()
        self.mouseX = 0
        self.mouseY = 0
        self.root = pygame.display.set_mode((600, 600), pygame.DOUBLEBUF)
        while 1:
            self.displayLoop()
    def displayLoop(self):
        self.root.fill((100,0,0))
        self.clock.tick(120)
        self.frame += 1
        self.handleMouseMove()
        self.eventLoop()
        pygame.display.flip() #used in pygame
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
                pass
            elif event.type == KEYUP:
                pass
            elif event.type == KEYDOWN:
                pass
    def handleMouseMove(self):
        mouseX = self.mouseX
        mouseY = self.mouseY
        textSurface = uiFont.render("X:"+str(mouseX)+" Y:"+str(mouseY), 1, uiTextcolor)
        self.root.fill((30, 30, 30), (mouseX + 6, mouseY + 5, textSurface.get_width(), textSurface.get_height()))
        self.root.blit(textSurface, (mouseX + 6, mouseY + 5, textSurface.get_width(), textSurface.get_height()))
        #pygame.draw.rect(self.root, pygame.Color(255, 255, 0), pygame.Rect(event.pos.x, event.pos.y, hhhhhh)
    def handleMouseClick(self, event):
        pass 
    def handleMouseRelease(self, event):
        pass

    def version(self):
        print(pygame.get_sdl_version())



if __name__ == "__main__":
    Arcade()
