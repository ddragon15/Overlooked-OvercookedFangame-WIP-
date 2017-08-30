# 1 - Import library
import pygame
from pygame.locals import *
import math
import random

import magic

import world
import player
import tiles
import items
#import sprites

# TODO collision checking on crates doesn't snap


if __name__ == "__main__":

    # 1 - Initialize the game
    pygame.init()

    # Initiate Player
    magic.player = player.Player()

    time = pygame.time.Clock()
    keyPressSpace = False


    magic.MTiles = [];
    magic.MItems = [];

    # Functions


    # 2 - Load images

    magic.MTiles.append(tiles.Crate(64,125))
    magic.MTiles.append(tiles.Crate(128,125))
    magic.MTiles.append(tiles.Crate(64*5,125))
    magic.MTiles.append(tiles.Storage(64*2,125+64,items.Onion))
    magic.MTiles.append(tiles.Storage(64*4,125+64,items.Tomato))
    magic.MTiles.append(tiles.cuttingBoard(64,125+64))

    magic.MItems.append(items.Plate(64,125))
    magic.MItems.append(items.Onion(128,125))
    magic.MItems.append(items.Tomato(64*5,125))



    # 4 - keep looping through
    while 1:
        ##badtimer -=1
        # 5 - clear the screen before drawing it again
        magic.mapScreen.fill(0)
        # 6 - draw the screen elements
        world.grassBuilder()

        for t in magic.MTiles:
            t.Update()
        for o in magic.MItems:
            o.Update()

        # 6.1 - Set player position and rotation
        magic.player.Update(magic.MTiles)

        # 6.4 - Draw DebugInfo
        font = pygame.font.Font(None, 24)
        # time = pygame.time.get_ticks()/600 #for the first Survivedtext
        time.tick()
        # survivedtext = font.render(str(math.floor(time)), True, (0,0,0))
        # survivedtext = font.render(str(magic.keyPress1), True, (0,0,0))
        survivedtext = font.render(str(math.floor(time.get_fps())), True, (0,0,0))
        textRect = survivedtext.get_rect()
        textRect.topright=[630,10]
        magic.mapScreen.blit(survivedtext, textRect)

        # 7 - update the screen
        pygame.display.flip()
        # 8 - loop through the events
        for event in pygame.event.get():
            # check if the event is the X button
            if event.type == KEYDOWN:
                if event.key == K_w:
                    magic.keyPress1 += 1
                if event.key == K_a:
                    magic.keyPress1 += 2
                if event.key == K_s:
                    magic.keyPress1 += 4
                if event.key == K_d:
                    magic.keyPress1 += 8
                if event.key == K_SPACE:
                    keyPressSpace = True
            if event.type == KEYUP:
                if event.key == K_w:
                    magic.keyPress1 -= 1
                if event.key == K_a:
                    magic.keyPress1 -= 2
                if event.key == K_s:
                    magic.keyPress1 -= 4
                if event.key == K_d:
                    magic.keyPress1 -= 8
                if event.key == K_SPACE:
                    magic.player.Grapper()
                    keyPressSpace = False

            # if event.type==pygame.MOUSEBUTTONDOWN:
            #     position=pygame.mouse.get_pos()

            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)
