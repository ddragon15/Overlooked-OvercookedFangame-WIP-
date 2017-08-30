import pygame
from pygame.locals import *
import math
import random
import inspect

import items
import magic
import player

class All():
    DebugBool = False
    DebugV = [0,0]
    rot = 0

    placeCheck = True
    itemHolding = None

    healthbar = pygame.image.load("resources/images/healthbar.jpg")
    health = pygame.image.load("resources/images/health.jpg")

    def Draw(self):
        playerrot = pygame.transform.rotate(self.image ,self.rot*90)
        playerpos1 = (self.pos[0], self.pos[1])
        magic.mapScreen.blit(playerrot, playerpos1)
        # pygame.draw.rect(magic.mapScreen, (50,50,131), pygame.Rect((x,y),(64,64)))

    def checkCollision(self, pos):
        boxrect = pygame.Rect((pos[0],pos[1]),(30,30))
        myRect = pygame.Rect((self.pos[0],self.pos[1]),(48,48))
        # self.DebugV[0] = pos[0]
        # self.DebugV[1] = pos[1]
        # self.DebugBool = True
        if myRect.colliderect(boxrect):
            return True
        else:
            return False

    def itemCheck(self):
        pos = [0,0]
        # go through items
        for i in magic.MItems:
            # if item collides with self storage
            if(All.checkCollision(self, i.pos) and i != magic.player.itemHolding):
                # object is there
                if not inspect.isclass(self.itemHolding):
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
        self.pos = [x,y]

    def Update(self):
        All.Draw(self)
        All.itemCheck(self)
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
        self.pos = [x,y]
        self.placeCheck = False

    def Update(self):
        All.Draw(self)
        # If empty create new Item
        if not All.itemCheck(self):
            magic.MItems.append(self.itemHolding(self.pos[0],self.pos[1]))

        All.Debug(self)

class cuttingBoard(All):
    process = 0

    def itemProcessor(self):
        if self.itemHolding != None and self.itemHolding.processable: #and not magic.player.checkHolding():
            print("Debug1")
            self.itemHolding.isOccupied = True
            self.placeCheck = False
            if self.process < 30:
                # Draw progress bar
                magic.mapScreen.blit(All.healthbar, (self.pos[0],self.pos[1]-5))
                for health1 in range(self.process*2):
                    magic.mapScreen.blit(All.health, (health1+self.pos[0]+1,self.pos[1]-4))
                return
            if self.process >= 30:
                self.itemHolding.isOccupied = False
                self.itemHolding.changeSkin()
                self.itemHolding.processable = False
                self.itemHolding = None
                self.process = 0
                self.placeCheck = True
        return


    spaceCheck = lambda self: self.process + 1

    def __init__(self, x, y):
        #super().__init__()
        self.image = pygame.image.load("resources/images/cuttingboard.jpg")
        self.rect = self.image.get_rect()
        self.pos = [x,y]
        self.rot = (random.randint(0, 4)*90)

    def Update(self):
        All.Draw(self)
        if All.itemCheck(self):
                self.itemProcessor()
        All.Debug(self)
