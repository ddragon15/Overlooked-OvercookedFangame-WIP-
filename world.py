import pygame
from pygame.locals import *

import magic

grass = pygame.image.load("resources/images/grass.png")

def grassBuilder():
    for x in range(int(magic.mapWidth/grass.get_width())+1):
        for y in range(int(magic.mapHeight/grass.get_height())+1):
            magic.mapScreen.blit(grass,(x*100,y*100))
