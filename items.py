import pygame
from pygame.locals import *
import math
import random

import magic

class All():
    DebugBool = False
    DebugV = [0,0]

    isHold = False
    isOccupied = False
    processable = True

    def Draw(self):
        playerrot = pygame.transform.rotate(self.image ,self.rot)
        playerpos1 = (self.pos[0]-32, self.pos[1]-32)
        magic.mapScreen.blit(playerrot, playerpos1)
        # pygame.draw.rect(magic.mapScreen, (50,50,131), pygame.Rect((x,y),(64,64)))

    def checkCollision(self, pos):
        boxrect = pygame.Rect((pos[0],pos[1]),(20,20))
        myRect = pygame.Rect((self.pos[0]-8,self.pos[1]-8),(34,34))
        # self.DebugV[0] = self.pos[0]-8
        # self.DebugV[1] = self.y-8
        # self.DebugBool = True
        boxrect.topleft = [pos[0],pos[1]]
        if myRect.colliderect(boxrect):
            return True
        else:
            return False

    def Debug(self):
        if self.DebugBool:
            pygame.draw.rect(magic.mapScreen, (50,250,131), pygame.Rect((self.DebugV[0],self.DebugV[1]),(34,34)))

    def setPos(self, pos):
        self.pos[0] = pos[0]
        self.pos[1] = pos[1]

class Onion(All):
    tag = "onion"

    def __init__(self, x, y):
        self.skin = "resources/images/onion.png"
        self.image = pygame.image.load(self.skin)
        # w,h = self.image.get_size()
        # self.image = pygame.transform.scale(self.image, (int(w),int(h)))
        # self.rect.topleft = [x,y]
        self.rect = self.image.get_rect()
        self.pos = [x+24,y+24]
        self.rot = random.randint(0, 360)*1

    def Update(self):
        All.Draw(self)
        All.Debug(self)

    def changeSkin(self):
        if self.skin is not "resource/image/onionS.png":
            self.skin = "resources/images/onionS.png"
            self.image = pygame.image.load(self.skin)
