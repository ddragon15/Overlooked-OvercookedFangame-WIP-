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




if __name__ == "__main__":

    # 1 - Initialize the game
    pygame.init()

    # Initiate Player
    player = player.Player()
    magic.player = player

    time = pygame.time.Clock()
    selectItem = None
    keyPressSpace = False


    magic.MTiles = [];
    magic.MItems = [];

    # Functions
    def HoldItem(selectItem):
        if keyPressSpace:
            if not player.CheckHolding():
                # Check if Item is in range
                for i in magic.MItems:
                    if(i.checkCollision(player.GetInfront(True)) and not i.isOccupied):
                        # Get that Item
                        selectItem = i
                        player.holding_item = True
                        i.isHold = True
                        return selectItem
                # TODO Brocken Code - spaceCheck for cuttingBoard
                # for t in magic.MTiles:
                #     if(t.checkCollision(player.GetInfront(True)) and dir("spaceCheck") == True):
                #         if t.isOccupied:
                #             t.spaceCheck()
                #             return selectItem

            elif(player.CheckHolding()):
                # Check for Crate
                for t in magic.MTiles:
                    if(t.checkCollision(player.GetInfront(True))):
                        if(t.placeCheck):
                            # Place the item
                            selectItem.x = t.x+24
                            selectItem.y = t.y+24
                            player.holding_item = False
                            selectItem.isHold = False
                            return None
                        else:
                            return selectItem
                # # Check for Item
                # for i in magic.MItems:
                #     if(i.checkCollision(player.GetInfront(True)) and not i.isHold):
                #         return None
                # drop it on the ground
                pos = player.GetInfront(True)
                selectItem.x = pos[0]
                selectItem.y = pos[1]
                player.holding_item = False
                selectItem.isHold = False
            # Bilanz
            return None

    # 2 - Load images

    magic.MTiles.append(tiles.Crate(64,125))
    magic.MTiles.append(tiles.Crate(128,125))
    magic.MTiles.append(tiles.Crate(64*5,125))
    magic.MTiles.append(tiles.Storage(64*2,125+64,items.Onion))
    magic.MTiles.append(tiles.cuttingBoard(64,125+64))

    magic.MItems.append(items.Onion(128,125))
    magic.MItems.append(items.Onion(64*5,125))



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
        player.Update(magic.MTiles)
        if selectItem is not None:
            selectItem.setPos(player.GetInfront(True))


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
                    selectItem = HoldItem(selectItem)
                    keyPressSpace = False

            # if event.type==pygame.MOUSEBUTTONDOWN:
            #     position=pygame.mouse.get_pos()

            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)
