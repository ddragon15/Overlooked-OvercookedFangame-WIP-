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
    holding_item = None

    halteentfernung = 45

    def __init__(self):
        #super().__init__()
        self.image = pygame.image.load("resources/images/cook1.png")
        self.rect = pygame.Rect((self.playerpos[0]-128,self.playerpos[1]-128),(64,64))


    def Draw(self):
        playerrot = pygame.transform.rotate(self.image , self.rotation)
        playerpos1 = (self.playerpos[0]-playerrot.get_rect().width/2, self.playerpos[1]-playerrot.get_rect().height/2)
        magic.mapScreen.blit(playerrot, playerpos1)

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

        self.rect.topleft = (x-32, y-32) #Collision Rectangle
        if not self.Collision(self.tiles):
            self.playerpos = [x,y]

    def getInfront(self):
        # pygame.draw.rect(magic.mapScreen, (11,31, 131), pygame.Rect((self.playerpos[0] + (self.infront[0]*self.halteentfernung),self.playerpos[1] + (self.infront[1]*self.halteentfernung)),(15,15)))
            pos = (self.playerpos[0]-8 + (self.infront[0]*self.halteentfernung),self.playerpos[1]-8 + (self.infront[1]*self.halteentfernung))
            return pos

    def Update(self, GTiles):
        self.tiles = GTiles;
        self.Move()
        if self.holding_item is not None:
            self.holding_item.setPos(self.getInfront())
        self.Draw()
        pos = self.getInfront()
        # pygame.draw.rect(magic.mapScreen, (20,50,231), pygame.Rect((pos[0],pos[1]),(20,20)))

    def ItemHandler(self):
        if not self.CheckHolding(): # if holding nothing
            # Check if Item is in range
            for i in magic.MItems:
                if(i.checkCollision(self.getInfront()) and not i.isOccupied):
                    # Get that Item
                    self.holding_item = i
                    i.isHold = True
                    return
            # TODO Brocken Code - spaceCheck for cuttingBoard
            # for t in magic.MTiles:
            #     if(t.checkCollision(player.getInfront()) and dir("spaceCheck") == True):
            #         if t.isOccupied:
            #             t.spaceCheck()
            #             return selectItem

        elif(self.CheckHolding()):
            # Check for Crate
            for t in magic.MTiles:
                if(t.checkCollision(self.getInfront())):
                    if(t.placeCheck):
                        # Place the item
                        self.holding_item.pos = [t.pos[0]+24,t.pos[1]+24]
                        self.holding_item.isHold = False
                        self.holding_item = None
                        return
                    else:
                        return
            # # Check for Item
            # for i in magic.MItems:
            #     if(i.checkCollision(player.getInfront()) and not i.isHold):
            #         return None
            # drop it on the ground
            self.holding_item.pos = self.getInfront()
            self.holding_item.isHold = False
            self.holding_item = None
        # Bilanz
        return

    def CheckHolding(self):
        if self.holding_item:
            return True
        else:
            return False

    def setHolding(self, holder):
        self.holding_item = holder
