import pygame
from pygame.locals import *
import math
import random

import items
import magic
import player

'''
storage = pygame.image.load("resources/images/storage.jpg")
crate = pygame.image.load("resources/images/crate.jpg")

'''

class All():
    DebugBool = False
    DebugV = [0,0]
    placeCheck = True

    itemHolding = None

    healthbar = pygame.image.load("resources/images/healthbar.jpg")
    health = pygame.image.load("resources/images/health.jpg")

    def Draw(self, img, x, y, rot):
        playerrot = pygame.transform.rotate(img ,rot*90)
        playerpos1 = (x, y)
        magic.mapScreen.blit(playerrot, playerpos1)
        # pygame.draw.rect(magic.mapScreen, (50,50,131), pygame.Rect((x,y),(64,64)))

    def checkCollision(self, pos):
        boxrect = pygame.Rect((pos[0],pos[1]),(30,30))
        myRect = pygame.Rect((self.x,self.y),(48,48))
        # self.DebugV[0] = pos[0]
        # self.DebugV[1] = pos[1]
        # self.DebugBool = True
        if myRect.colliderect(boxrect):
            return True
        else:
            return False

    def spaceChecker(self):
        for i in magic.MItems:
            pos = [i.x,i.y]
            if not i.isHold:
                if(self.checkCollision(pos)):
                    self.placeCheck = False
                    self.itemHolding = i
                    return
        self.placeCheck = True
        self.itemOccupied = None

    def itemCheck(self):
        pos = [0,0]
        checker = False
        # go through items
        for i in magic.MItems:
            # if item collides with self storage
            pos[0] = i.x
            pos[1] = i.y
            if(All.checkCollision(self, pos) and i.tag == self.item):
                # object is there
                self.itemHolding = i
                return True
                break
        return False

    def Debug(self):
        if self.DebugBool:
            pygame.draw.rect(magic.mapScreen, (50,250,131), pygame.Rect((self.DebugV[0],self.DebugV[1]),(25,25)))

class Crate(All):

    def __init__(self, x, y):
        #super().__init__()
        self.image = pygame.image.load("resources/images/crate.jpg")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def Update(self):
        All.Draw(self, self.image, self.x, self.y, 0)
        All.spaceChecker(self)
        All.Debug(self)

class Storage(All):
    #
    # def ItemChoose(self):
    #     #check wich item
    #     if(self.item == "Onion"):



    def __init__(self, x, y, item):
        #super().__init__()
        self.image = pygame.image.load("resources/images/storage.jpg")
        self.rect = self.image.get_rect()
        self.itemHolding = item #Holding = Blueprint to place
        print(str(self.itemHolding))
        self.x = x
        self.y = y
        self.placeCheck = False

    def Update(self):
        All.Draw(self, self.image, self.x, self.y, 0)
        # If empty create new Item
        if All.itemCheck(self):
            magic.MItems.append(self.itemHolding(self.x,self.y))

        All.Debug(self)

class cuttingBoard(All):
    itemInProcess = False
    process = 0


    def itemHandler(self):
        # Check if item is on Surface
        pos = [0,0]
        checker = False
        # go through items
        for i in magic.MItems:
            # if item collides with self
            pos[0] = i.x
            pos[1] = i.y
            if(All.checkCollision(self, pos) and i.processable):
                # object is there
                checker = True
                i.isOccupied = True
                self.itemInProcess = i
                break
        # Process Food


        if self.itemInProcess != None:
            if self.process < 30:
                # Draw progress bar
                magic.mapScreen.blit(All.healthbar, (self.x,self.y-5))
                for health1 in range(self.process*2):
                    magic.mapScreen.blit(All.health, (health1+self.x+1,self.y-4))
            if self.process >= 30:
                self.itemInProcess.isOccupied = False
                self.itemInProcess.changeSkin()
                self.itemInProcess.processable = False


        if not checker:
            self.process = 0
            self.itemInProcess = None
            return

    # def spaceCheck(self):
    #     self.process += 1
    # Lamda function test
    spaceCheck = lambda self: self.process + 1

    def __init__(self, x, y):
        #super().__init__()
        self.image = pygame.image.load("resources/images/cuttingBoard.jpg")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rot = (random.randint(0, 4)*90)

    def Update(self):
        All.Draw(self, self.image, self.x, self.y, self.rot)
        self.itemHandler()
        All.Debug(self)
