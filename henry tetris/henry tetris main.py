import numpy as np
import pygame
from pygame.locals import *
from htBlocks import *
from htSystem import *
import sys
from random import *

# 2 - Define constants
screen_width = 300
screen_height = 400
scale = screen_height/400
edge = screen_height/20*10
FRAMES_PER_SECOND = 60
time = 0

# 3 - Initialize the world
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sound(s),  etc.
colors = ["blue", "red", "yellow", "green", "orange"]

# 5 - Initialize variables
newColor = choice(colors)
oldColor = newColor
movingBlock = iBlock(screen,edge/2,10,newColor,scale)
stationaryBlocks = []

# 6 - Loop forever
while True:
    time+=1
    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program 
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_UP:
                movingBlock.rotateClockwise()
            elif event.key == pygame.K_LEFT:
                failure = False
                for block in movingBlock.blocks:
                    if block.x < 20:
                        failure = True
                    for sblock in stationaryBlocks:
                        if block.x < sblock.x + 25 and abs(block.y-sblock.y) < 2:
                            failure = True
                if not failure:
                    movingBlock.moveLeft()
            elif event.key == pygame.K_RIGHT:
                failure = False
                for block in movingBlock.blocks:
                    if block.x > edge-20:
                        failure = True
                    for sblock in stationaryBlocks:
                        if block.x > sblock.x - 25 and abs(block.y-sblock.y) < 2:
                            failure = True
                if not failure:
                    movingBlock.moveRight()
            elif event.key == pygame.K_p:
                yval = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0}
                for block in stationaryBlocks:
                    print(type(block), block.x, block.y)
                    yval[int((screen_height-(block.y+10))/20)] = yval[int((screen_height-(block.y+10))/20)]+1
                    print(int((screen_height-(block.y+10))/20), yval[int((screen_height-(block.y+10))/20)], block.y, screen_height)
                    print(len(stationaryBlocks))

    # 8 - Do any "per frame" actions
    if time%20 == 0:
        found = False
        for block in movingBlock.blocks:
            if block.y >= screen_height - 10:
                for bLock in movingBlock.blocks:
                    stationaryBlocks.append(bLock)
                while newColor == oldColor:
                    newColor = choice(colors)
                oldColor = newColor
                movingBlock = randomBlock(screen,edge,newColor)
                found = True
                break
        for block in movingBlock.blocks:
            for sblock in stationaryBlocks:
                if block.y >= sblock.y - block.dim and abs(block.x-sblock.x)<3 and not found:
                    for bLock in movingBlock.blocks:
                        stationaryBlocks.append(bLock)
                    while newColor == oldColor:
                        newColor = choice(colors)
                    oldColor = newColor
                    movingBlock = randomBlock(screen,edge,newColor)
                    found = True
                    break
                if found:
                    break
        movingBlock.y += screen_height/20
    if (movingBlock.x-scale*10)%(scale*20) != 0:
        if (movingBlock.x-scale*10)%(scale*20) < scale*10:
            movingBlock.x -= (movingBlock.x-scale*10)%(scale*20)
        else:
            movingBlock.x += 20-(movingBlock.x-scale*10)%(scale*20)
    for block in movingBlock.blocks:
        if block.x < 0:
            movingBlock.x = 10 - (block.x-movingBlock.x)
            break
        elif block.x > edge:
            movingBlock.x = edge - 10 - (block.x-movingBlock.x)
            break
    yval = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0}
    falling = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0}
    for block in stationaryBlocks:
        yval[int((screen_height-(block.y+10))/20)] = yval[int((screen_height-(block.y+10))/20)]+1
    for i in range(20):
        if yval[i] >= 10:
            for block in stationaryBlocks:
                if int((screen_height-(block.y+10))/20) == i:
                    stationaryBlocks.remove(block)
                    del block
            for j in range(i+1, 20):
                falling[j] +=1
    for block in stationaryBlocks:
        if not int((screen_height-(block.y+10))/20) < 0:
            block.y += falling[int((screen_height-(block.y+10))/20)]*20

    # 9 - Clear the window
    screen.fill((50,50,50))
    drawGrid(int(edge),int(screen_height),screen,(150,150,150))
    # 10 - Draw all window elements
    for block in stationaryBlocks:
        block.render()
    movingBlock.render()
    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
