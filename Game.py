#!/usr/bin/env python
# coding=utf-8

from random import randint
import math
import copy

class Game:
    """
    Game 2048 
    """
    
    SIZE = 5
    DEBUG = False
    DEBUG_STEP_BY_STEP = False
    
    RESULT_MOVED = 0
    RESULT_NOT_MOVED = 1
    RESULT_GAME_OVER = 2
    
    map = None
    statsMoves = 0
    statsScore = 0
    
    def __init__(self, ):
        self.map = [[0 for x in range(self.SIZE)] for x in range(self.SIZE)] 
        self.spawnTile()
        self.spawnTile()
        
    def slide(self, side):
        slideX = int(math.cos(side * math.pi/2))
        slideY = int(math.sin(side * math.pi/2))
        
        moved = False
        
        fx = self.SIZE-1 if slideX > 0 else 0
        fy = self.SIZE-1 if slideY > 0 else 0
        tx = 0-1 if slideX > 0 else self.SIZE
        ty = 0-1 if slideY > 0 else self.SIZE
        for x in xrange(fx, tx, -1 if fx > tx else 1):
            for y in xrange(fy, ty, -1 if fy > ty else 1):
                if self.slideTile(x, y, slideX, slideY):
                    moved = True
        
        if moved:
        
            self.statsMoves += 1
        
            if self.DEBUG:
                self.printMap()
                if self.DEBUG_STEP_BY_STEP:
                    raw_input()
            
            self.spawnTile()
            
            if self.isGameOver():
                return self.RESULT_GAME_OVER
            else:
                return self.RESULT_MOVED
        else:
            if self.isGameOver():
                return self.RESULT_GAME_OVER
            else:  
                return self.RESULT_NOT_MOVED
    
    def slideTile(self, x, y, slideX, slideY):
        if not self.isTileEmpty(x, y):
            moved = False
            
            tx = x + slideX
            ty = y + slideY
            
            #move tile until hit something
            while tx >= 0 and tx < self.SIZE and ty >= 0 and ty < self.SIZE and self.isTileEmpty(tx, ty):
                ox = x
                oy = y
                x = tx
                y = ty
                tx = x + slideX
                ty = y + slideY
                
                self.map[x][y] = self.map[ox][oy]
                self.map[ox][oy] = 0
                moved = True
                
            #connect same tiles
            if tx >= 0 and tx < self.SIZE and ty >= 0 and ty < self.SIZE:
                val = self.map[x][y] 
                if self.map[tx][ty] == val:
                    self.map[tx][ty] = val * 2
                    self.map[x][y] = 0
                    self.statsScore += val * 2
                    
            return moved
    
    def spawnTile(self):
        
        emptyTiles = []
        
        for x in range(0, self.SIZE):
            for y in range(0, self.SIZE):
                if self.isTileEmpty(x, y):
                    emptyTiles.append((x, y))
        
        if len(emptyTiles) > 0:
            emptyTile = emptyTiles[randint(0, len(emptyTiles) - 1)]
            
            val = randint(0, 4)
            if val < 3:
                val = 2
            else:
                val = 4
            
            self.map[emptyTile[0]][emptyTile[1]] = val

    def isTileEmpty(self, x, y):
        return self.map[x][y] == 0
    
    def isGameOver(self):
        
        for x in range(0, self.SIZE):
            for y in range(0, self.SIZE):
                if self.isTileEmpty(x, y):
                    return False
        return True
    
    def printMap(self):
        print #empty line
        self.printMapTableLine()  
        
        for y in range(0, self.SIZE):
            line = '|'
            for x in range(0, self.SIZE):
                line += str(self.map[x][y]).ljust(4, ' ') + '|'
            print line
            
            self.printMapTableLine()
        
    def printMapTableLine(self):
        line = '+'
        for i in range(0, self.SIZE):
            line += '----+'
        print line
    
    def getStats(self):
        largestTile = 0
        
        for y in range(0, self.SIZE):
            for x in range(0, self.SIZE):
                if self.map[x][y] > largestTile:
                    largestTile = self.map[x][y]
        
        return (self.statsMoves, self.statsScore, largestTile)
    
    pushValues = []
    
    def push(self):
        self.pushValues.append((copy.deepcopy(self.map), self.statsMoves, self.statsScore))
    
    def pop(self):
        self.map, self.statsMoves, self.statsScore = self.pushValues.pop()
    
    def getPushedScore(self):
        ma, mv, score = self.pushValues[-1]
        return score
