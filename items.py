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
        myRect = pygame.Rect((self.pos[0]-16,self.pos[1]-16),(34,34))
        # self.DebugV = myRect
        # self.DebugBool = True
        boxrect.topleft = [pos[0],pos[1]]
        if myRect.colliderect(boxrect):
            return True
        else:
            return False

    def Debug(self):
        if self.DebugBool:
            pygame.draw.rect(magic.mapScreen, (50,250,131), self.DebugV)
        # self.DebugV[0] = self.pos[0]-8
        # self.DebugV[1] = self.y-8
        # self.DebugBool = True

    def setPos(self, pos):
        self.pos = [pos[0]+8,pos[1]+8]

class Onion(All):
    tag = "onion"

    def __init__(self, x, y):
        self.skin = "resources/images/onion.png"
        self.image = pygame.image.load(self.skin)
        # w,h = self.image.get_size()
        # self.image = pygame.transform.scale(self.image, (int(w),int(h)))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        self.pos = [x+32,y+32]
        self.rot = 0 #random.randint(0, 360)*1

    def Update(self):
        All.Draw(self)
        All.Debug(self)

    def changeSkin(self):
        if self.skin is not "resource/image/onionS.png":
            self.skin = "resources/images/onionS.png"
            self.image = pygame.image.load(self.skin)

class Tomato(All):
    tag = "tomato"

    def __init__(self, x, y):
        self.skin = "resources/images/tomato.png"
        self.image = pygame.image.load(self.skin)
        # w,h = self.image.get_size()
        # self.image = pygame.transform.scale(self.image, (int(w),int(h)))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        self.pos = [x+32,y+32]
        self.rot = 0 #random.randint(0, 360)*1

    def Update(self):
        All.Draw(self)
        All.Debug(self)

    def changeSkin(self):
        if self.skin is not "resource/image/tomatoS.png":
            self.skin = "resources/images/tomatoS.png"
            self.image = pygame.image.load(self.skin)

class Lettuce(All):
    tag = "lettuce"

    def __init__(self, x, y):
        self.skin = "resources/images/lettuce.png"
        self.image = pygame.image.load(self.skin)
        # w,h = self.image.get_size()
        # self.image = pygame.transform.scale(self.image, (int(w),int(h)))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        self.pos = [x+32,y+32]
        self.rot = 0 #random.randint(0, 360)*1

    def Update(self):
        All.Draw(self)
        All.Debug(self)

    def changeSkin(self):
        if self.skin is not "resource/image/lettuceS.png":
            self.skin = "resources/images/lettuceS.png"
            self.image = pygame.image.load(self.skin)

class Plate(All):
    processable = False
    # TODO make states for different Foods

    def __init__(self, x, y):
        self.skin = "resources/images/plate.png"
        self.image = pygame.image.load(self.skin)
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        self.pos = [x+32,y+32]
        self.rot = 0

    def Update(self):
        All.Draw(self)
        All.Debug(self)


    # TODO Plate states
    # If an item sits ontop of the Plate
        # Loop through Combinations out of all incedience onto the plate plus the new one
            # Take the first one all incredience work on
        # Consume the item (delete it)
        # Change Skin

    # TODO Make a map out of all recipies (maybe in another File)
        # Which items are needet?
        # Can it be processed by something?
        # Which state is the plate in? Choose Skin for swap and return it
