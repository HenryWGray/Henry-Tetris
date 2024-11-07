import numpy as np
import pygame
from random import randint
class Block():
    def __init__(self, screen, x, y, color, scale, number = 0):
        self.x = x
        self.y = y
        self.scale = scale
        self.color = color
        self.screen = screen
        self.dim = self.scale*20
        self.number = number
    def render(self):
        dim = self.scale*20
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x-dim/2, self.y-dim/2, dim, dim))
        pygame.draw.rect(self.screen, "black", pygame.Rect(self.x-dim/2, self.y-dim/2, dim, dim),2)

class tBlock():
    def __init__(self, screen, x, y, color, scale):
        self.screen = screen
        self.x = x
        self.y = y
        self.lastx = x
        self.lasty = y
        self.color = color
        self.scale = scale
        self.blocks = []
        self.blockAngle = -np.pi/2
        for i in range(4):
            if i == 0:
                self.blocks.append(Block(screen, self.x, self.y, self.color, self.scale))
                blockAngle = 0
            else:
                self.blocks.append(Block(screen, self.x+np.cos(blockAngle)*20, self.y+np.sin(blockAngle)*20, self.color, self.scale))
                blockAngle += np.pi/2
    def update(self):
        i=0
        for block in self.blocks:
            block.x += self.x-self.lastx
            block.y += self.y-self.lasty
            if i != 0:
                self.blocks[i].x, self.blocks[i].y = self.x + np.cos(self.blockAngle+np.pi/2*i)*20, self.y + np.sin(self.blockAngle+np.pi/2*i)*20
            else:
                self.blocks[i].x, self.blocks[i].y = self.x, self.y
            i+=1
        
        self.lastx = self.x
        self.lasty = self.y
    def render(self):
        i=0
        for block in self.blocks:
            block.x += self.x-self.lastx
            block.y += self.y-self.lasty
            if i != 0:
                self.blocks[i].x, self.blocks[i].y = self.x + np.cos(self.blockAngle+np.pi/2*i)*20, self.y + np.sin(self.blockAngle+np.pi/2*i)*20
            i+=1
            block.render()
        self.lastx = self.x
        self.lasty = self.y
    def rotateClockwise(self):
        self.blockAngle += np.pi/2
        if self.blockAngle == 2*np.pi:
            self.blockAngle = 0
    def moveLeft(self):
        self.x-=self.scale*20
    def moveRight(self):
        self.x+=self.scale*20

class lBlock():
    def __init__(self, screen, x, y, color, scale):
        self.screen = screen
        self.x = x
        self.y = y
        self.lastx = x
        self.lasty = y
        self.color = color
        self.scale = scale
        self.blocks = []
        self.blockAngle = 0
        self.shape = [[0,1,0],[0,1,0],[0,1,1]]
        k=0
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j] == 1:
                    self.blocks.append(Block(screen, self.x+(j-1)*20, self.y+(i-1)*20, self.color, self.scale, k))
                    k+=1
    def update(self):
        k=0
        for block in self.blocks:
            for i in range(len(self.shape)):
                for j in range(len(self.shape[i])):
                    if self.shape[i][j] == 1:
                        if block.number == k:
                            block.x, block.y = self.x+(j-1)*20, self.y+(i-1)*20
                        k+=1
            k=0
            
        self.lastx = self.x
        self.lasty = self.y
    def render(self):
        k=0
        for block in self.blocks:
            block.x += self.x-self.lastx
            block.y += self.y-self.lasty
            for i in range(len(self.shape)):
                for j in range(len(self.shape[i])):
                    if self.shape[i][j] == 1:
                        if block.number == k:
                            
                            block.x, block.y = self.x+(j-1)*20, self.y+(i-1)*20
                        k+=1
            k = 0
            block.render()
        self.lastx = self.x
        self.lasty = self.y
    def rotateClockwise(self):
        self.blockAngle += 1
        if self.blockAngle == 4:
            self.blockAngle = 0
        if self.blockAngle == 0:
            self.shape = [[0,1,0],[0,1,0],[0,1,1]]
        elif self.blockAngle == 1:
            self.shape = [[0,0,0],[1,1,1],[1,0,0]]
        elif self.blockAngle == 2:
            self.shape = [[1,1,0],[0,1,0],[0,1,0]]
        elif self.blockAngle == 3:
            self.shape = [[0,0,1],[1,1,1],[0,0,0]]
    def moveLeft(self):
        self.x-=self.scale*20
    def moveRight(self):
        self.x+=self.scale*20

class jBlock():
    def __init__(self, screen, x, y, color, scale):
        self.screen = screen
        self.x = x
        self.y = y
        self.lastx = x
        self.lasty = y
        self.color = color
        self.scale = scale
        self.blocks = []
        self.blockAngle = 0
        self.shape = [[0,1,0],[0,1,0],[1,1,0]]
        k=0
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j] == 1:
                    self.blocks.append(Block(screen, self.x+(j-1)*20, self.y+(i-1)*20, self.color, self.scale, k))
                    k+=1
    def update(self):
        k=0
        for block in self.blocks:
            for i in range(len(self.shape)):
                for j in range(len(self.shape[i])):
                    if self.shape[i][j] == 1:
                        if block.number == k:
                            block.x, block.y = self.x+(j-1)*20, self.y+(i-1)*20
                        k+=1
            k=0
            
        self.lastx = self.x
        self.lasty = self.y
    def render(self):
        k=0
        for block in self.blocks:
            block.x += self.x-self.lastx
            block.y += self.y-self.lasty
            for i in range(len(self.shape)):
                for j in range(len(self.shape[i])):
                    if self.shape[i][j] == 1:
                        if block.number == k:
                            
                            block.x, block.y = self.x+(j-1)*20, self.y+(i-1)*20
                        k+=1
            k = 0
            block.render()
        self.lastx = self.x
        self.lasty = self.y
    def rotateClockwise(self):
        self.blockAngle += 1
        if self.blockAngle == 4:
            self.blockAngle = 0
        if self.blockAngle == 0:
            self.shape = [[0,1,0],[0,1,0],[1,1,0]]
        elif self.blockAngle == 1:
            self.shape = [[1,0,0],[1,1,1],[0,0,0]]
        elif self.blockAngle == 2:
            self.shape = [[0,1,1],[0,1,0],[0,1,0]]
        elif self.blockAngle == 3:
            self.shape = [[0,0,0],[1,1,1],[0,0,1]]
    def moveLeft(self):
        self.x-=self.scale*20
    def moveRight(self):
        self.x+=self.scale*20

class oBlock():
    def __init__(self, screen, x, y, color, scale):
        self.screen = screen
        self.x = x
        self.y = y
        self.lastx = x
        self.lasty = y
        self.color = color
        self.scale = scale
        self.blocks = []
        self.blockAngle = 0
        self.shape = [[0,1,1],[0,1,1],[0,0,0]]
        k=0
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j] == 1:
                    self.blocks.append(Block(screen, self.x+(j-1)*20, self.y+(i-1)*20, self.color, self.scale, k))
                    k+=1
    def update(self):
        k=0
        for block in self.blocks:
            for i in range(len(self.shape)):
                for j in range(len(self.shape[i])):
                    if self.shape[i][j] == 1:
                        if block.number == k:
                            block.x, block.y = self.x+(j-1)*20, self.y+(i-1)*20
                        k+=1
            k=0
            
        self.lastx = self.x
        self.lasty = self.y
    def render(self):
        k=0
        for block in self.blocks:
            block.x += self.x-self.lastx
            block.y += self.y-self.lasty
            for i in range(len(self.shape)):
                for j in range(len(self.shape[i])):
                    if self.shape[i][j] == 1:
                        if block.number == k:
                            
                            block.x, block.y = self.x+(j-1)*20, self.y+(i-1)*20
                        k+=1
            k = 0
            block.render()
        self.lastx = self.x
        self.lasty = self.y
    def rotateClockwise(self):
        self.blockAngle += 0
        if self.blockAngle == 4:
            self.blockAngle = 0
        if self.blockAngle == 0:
            self.shape = [[0,1,1],[0,1,1],[0,0,0]]
    def moveLeft(self):
        self.x-=self.scale*20
    def moveRight(self):
        self.x+=self.scale*20

class sBlock():
    def __init__(self, screen, x, y, color, scale):
        self.screen = screen
        self.x = x
        self.y = y
        self.lastx = x
        self.lasty = y
        self.color = color
        self.scale = scale
        self.blocks = []
        self.blockAngle = 0
        self.shape = [[0,1,1],[1,1,0],[0,0,0]]
        k=0
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j] == 1:
                    self.blocks.append(Block(screen, self.x+(j-1)*20, self.y+(i-1)*20, self.color, self.scale, k))
                    k+=1
    def update(self):
        k=0
        for block in self.blocks:
            for i in range(len(self.shape)):
                for j in range(len(self.shape[i])):
                    if self.shape[i][j] == 1:
                        if block.number == k:
                            block.x, block.y = self.x+(j-1)*20, self.y+(i-1)*20
                        k+=1
            k=0
            
        self.lastx = self.x
        self.lasty = self.y
    def render(self):
        k=0
        for block in self.blocks:
            block.x += self.x-self.lastx
            block.y += self.y-self.lasty
            for i in range(len(self.shape)):
                for j in range(len(self.shape[i])):
                    if self.shape[i][j] == 1:
                        if block.number == k:
                            
                            block.x, block.y = self.x+(j-1)*20, self.y+(i-1)*20
                        k+=1
            k = 0
            block.render()
        self.lastx = self.x
        self.lasty = self.y
    def rotateClockwise(self):
        self.blockAngle += 1
        if self.blockAngle == 4:
            self.blockAngle = 0
        if self.blockAngle == 0:
            self.shape = [[0,1,1],[1,1,0],[0,0,0]]
        elif self.blockAngle == 1:
            self.shape = [[0,1,0],[0,1,1],[0,0,1]]
        elif self.blockAngle == 2:
            self.shape = [[0,0,0],[0,1,1],[1,1,0]]
        elif self.blockAngle == 3:
            self.shape = [[1,0,0],[1,1,0],[0,1,0]]
    def moveLeft(self):
        self.x-=self.scale*20
    def moveRight(self):
        self.x+=self.scale*20

class zBlock():
    def __init__(self, screen, x, y, color, scale):
        self.screen = screen
        self.x = x
        self.y = y
        self.lastx = x
        self.lasty = y
        self.color = color
        self.scale = scale
        self.blocks = []
        self.blockAngle = 0
        self.shape = [[1,1,0],[0,1,1],[0,0,0]]
        k=0
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j] == 1:
                    self.blocks.append(Block(screen, self.x+(j-1)*20, self.y+(i-1)*20, self.color, self.scale, k))
                    k+=1
    def update(self):
        k=0
        for block in self.blocks:
            for i in range(len(self.shape)):
                for j in range(len(self.shape[i])):
                    if self.shape[i][j] == 1:
                        if block.number == k:
                            block.x, block.y = self.x+(j-1)*20, self.y+(i-1)*20
                        k+=1
            k=0
            
        self.lastx = self.x
        self.lasty = self.y
    def render(self):
        k=0
        for block in self.blocks:
            block.x += self.x-self.lastx
            block.y += self.y-self.lasty
            for i in range(len(self.shape)):
                for j in range(len(self.shape[i])):
                    if self.shape[i][j] == 1:
                        if block.number == k:
                            
                            block.x, block.y = self.x+(j-1)*20, self.y+(i-1)*20
                        k+=1
            k = 0
            block.render()
        self.lastx = self.x
        self.lasty = self.y
    def rotateClockwise(self):
        self.blockAngle += 1
        if self.blockAngle == 4:
            self.blockAngle = 0
        if self.blockAngle == 0:
            self.shape = [[1,1,0],[0,1,1],[0,0,0]]
        elif self.blockAngle == 1:
            self.shape = [[0,0,1],[0,1,1],[0,1,0]]
        elif self.blockAngle == 2:
            self.shape = [[0,0,0],[1,1,0],[0,1,1]]
        elif self.blockAngle == 3:
            self.shape = [[0,0,1],[0,1,1],[0,1,0]]
    def moveLeft(self):
        self.x-=self.scale*20
    def moveRight(self):
        self.x+=self.scale*20

class iBlock():
    def __init__(self, screen, x, y, color, scale):
        self.screen = screen
        self.x = x
        self.y = y
        self.lastx = x
        self.lasty = y
        self.color = color
        self.scale = scale
        self.blocks = []
        self.blockAngle = 0
        self.shape = [[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0]]
        k=0
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j] == 1:
                    self.blocks.append(Block(screen, self.x+(j-1)*20, self.y+(i-1)*20, self.color, self.scale, k))
                    k+=1
    def update(self):
        k=0
        for block in self.blocks:
            for i in range(len(self.shape)):
                for j in range(len(self.shape[i])):
                    if self.shape[i][j] == 1:
                        if block.number == k:
                            block.x, block.y = self.x+(j-1)*20, self.y+(i-1)*20
                        k+=1
            k=0
            
        self.lastx = self.x
        self.lasty = self.y
    def render(self):
        k=0
        for block in self.blocks:
            block.x += self.x-self.lastx
            block.y += self.y-self.lasty
            for i in range(len(self.shape)):
                for j in range(len(self.shape[i])):
                    if self.shape[i][j] == 1:
                        if block.number == k:
                            
                            block.x, block.y = self.x+(j-1)*20, self.y+(i-1)*20
                        k+=1
            k = 0
            block.render()
        self.lastx = self.x
        self.lasty = self.y
    def rotateClockwise(self):
        self.blockAngle += 1
        if self.blockAngle == 4:
            self.blockAngle = 0
        if self.blockAngle == 0:
            self.shape = [[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0]]
        elif self.blockAngle == 1:
            self.shape = [[0,0,0,0],[0,0,0,0],[1,1,1,1],[0,0,0,0]]
        elif self.blockAngle == 2:
            self.shape = [[0,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,0]]
        elif self.blockAngle == 3:
            self.shape = [[0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0]]
    def moveLeft(self):
        self.x-=self.scale*20
    def moveRight(self):
        self.x+=self.scale*20

def randomBlock(screen, screen_width,color):
    choice = randint(0,6)
    if choice == 0:
        return(tBlock(screen,screen_width/2,10,color,1))
    elif choice == 1:
        return(iBlock(screen,screen_width/2,10,color,1))
    elif choice == 2:
        return(jBlock(screen,screen_width/2,10,color,1))
    elif choice == 3:
        return(lBlock(screen,screen_width/2,10,color,1))
    elif choice == 4:
        return(oBlock(screen,screen_width/2,10,color,1))
    elif choice == 5:
        return(sBlock(screen,screen_width/2,10,color,1))
    elif choice == 6:
        return(zBlock(screen,screen_width/2,10,color,1))