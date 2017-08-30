import pygame
from pygame.locals import *
import math
import random

import magic

class Player(pygame.sprite.Sprite):
    player_speed = 3
    playerpos=[100,300]
    rotation = 0;
    playerrot = 0;
    infront = (0,0)

    itemHolding = None

    halteentfernung = 45

    def __init__(self):
        #super().__init__()
        self.image = pygame.image.load("resources/images/cook1.png")
        self.rect = pygame.Rect((self.playerpos[0]-16,self.playerpos[1]-16),(40,40))


    def Draw(self):
        playerrot = pygame.transform.rotate(self.image , self.rotation)
        playerpos1 = (self.playerpos[0]-playerrot.get_rect().width/2, self.playerpos[1]-playerrot.get_rect().height/2)
        magic.mapScreen.blit(playerrot, playerpos1)
        # pygame.draw.rect(magic.mapScreen, (11,31, 131), self.rect)

    def Collision(self, tiles):
        for o in tiles:
            boxrect = pygame.Rect(o.image.get_rect())
            boxrect.topleft = [o.pos[0],o.pos[1]]
            if self.rect.colliderect(boxrect):
                return True
        return False

    def Move(self):
        spd = self.player_speed
        x = self.playerpos[0]
        y = self.playerpos[1]

        # Move player
        if magic.keyPress1 == 1 and y > 0:
            y -= spd
            self.rotation = 0
            self.infront = (0,-1)
        elif magic.keyPress1 == 3 and y > 0 and x > 0:
            y -= spd
            x -= spd
            self.rotation = 45
            self.infront = (-0.75,-0.75)
        elif magic.keyPress1 == 2 and x > 0:
            x -= spd
            self.rotation = 90
            self.infront = (-1,0)
        elif magic.keyPress1 == 4 and y < magic.mapHeight:
            y += spd
            self.rotation = 180
            self.infront = (0,1)
        elif magic.keyPress1 == 6 and x > 0 and y < magic.mapHeight:
            y += spd
            x -= spd
            self.rotation = 135
            self.infront = (-0.75,0.75)
        elif magic.keyPress1 == 8 and x < magic.mapWidth:
            x += spd
            self.rotation = 270
            self.infront = (1,0)
        elif magic.keyPress1 == 9 and x < magic.mapWidth  and y > 0:
            y -= spd
            x += spd
            self.rotation = 315
            self.infront = (0.75,-0.75)
        elif magic.keyPress1 == 12 and x < magic.mapWidth and y < magic.mapHeight:
            y += spd
            x += spd
            self.rotation = 220
            self.infront = (0.75,0.75)

        self.rect.topleft = (x-20, y-16) #Collision Rectangle
        if not self.Collision(self.tiles):
            self.playerpos = [x,y]

    def getInfront(self):
        pos = (self.playerpos[0]-8 + (self.infront[0]*self.halteentfernung),self.playerpos[1]-8 + (self.infront[1]*self.halteentfernung))
        # pygame.draw.rect(magic.mapScreen, (11,31, 131), pygame.Rect(pos,(15,15)))
        return pos

    def Grapper(self):
        # TODO add plate decition

        if not self.checkHolding(): # if holding nothing
            # Check if Item is in range
            for i in magic.MItems:
                if i.checkCollision(self.getInfront()) and not i.isOccupied:
                    # Get that Item
                    self.itemHolding = i
                    i.isHold = True
                    break
            for t in magic.MTiles:
                if t.checkCollision(i.pos) and i.isHold and not t.isStorage:
                    t.itemHolding = None
                    return
                if t.checkCollision(self.getInfront()) and hasattr(t, "process") and t.itemHolding != None:
                    t.process += 1
                    return

        elif(self.checkHolding()): # if holding something
            # Check for Crate
            for t in magic.MTiles:
                if t.checkCollision(self.getInfront()):
                    if t.placeCheck and t.itemHolding == None:
                        # Place the item
                        self.itemHolding.pos = [t.pos[0]+32,t.pos[1]+32]
                        t.itemHolding = self.itemHolding
                        self.itemHolding.isHold = False
                        self.itemHolding = None
                        return
                    else:
                        return
            self.itemHolding.pos = self.getInfront()
            self.itemHolding.isHold = False
            self.itemHolding = None
        # Bilanz
        return
    # TODO redundenz
    def checkHolding(self):
        if self.itemHolding:
            return True
        else:
            return False
    # TODO redundenz
    def setHolding(self, holder):
        self.itemHolding = holder

    def Update(self, GTiles):
        self.tiles = GTiles;
        self.Move()
        if self.itemHolding is not None:
            self.itemHolding.setPos(self.getInfront())
        self.Draw()
        pos = self.getInfront()
        # pygame.draw.rect(magic.mapScreen, (20,50,231), pygame.Rect((pos[0],pos[1]),(20,20)))
