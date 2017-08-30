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
    holding_item = False

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
            self.playerpos[0] = x
            self.playerpos[1] = y

    def GetInfront(self, test):
        # pygame.draw.rect(magic.mapScreen, (11,31, 131), pygame.Rect((self.playerpos[0] + (self.infront[0]*self.halteentfernung),self.playerpos[1] + (self.infront[1]*self.halteentfernung)),(15,15)))
        if not test:
            return (self.infront[0]*self.halteentfernung,self.infront[1]*self.halteentfernung)
        else:
            pos = (self.playerpos[0]-8 + (self.infront[0]*self.halteentfernung),self.playerpos[1]-8 + (self.infront[1]*self.halteentfernung))
            return pos

    def Update(self, GTiles):
        self.tiles = GTiles;
        self.Move()
        self.Draw()
        pos = self.GetInfront(True)
        # pygame.draw.rect(magic.mapScreen, (20,50,231), pygame.Rect((pos[0],pos[1]),(20,20)))


    def CheckHolding(self):
        if self.holding_item:
            return True
        else:
            return False

    def setHolding(self, holder):
        self.holding_item = holder
