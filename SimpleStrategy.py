#!/usr/bin/env python
# coding=utf-8

from RandomStrategy import RandomStrategy
from random import randint
import math
import copy
                            
class SimpleStrategy(RandomStrategy):
    """
    SimpleStrategy for Game 2048 
    """
    
    PRICE_SCORE = 1.0
    
    def play(self):
        
        result = 0
        
        while result != 2:
            bestPrice = 0
            bestPriceSide = None
            
            for side in range(0, 4):
                
                self.game.push()
                
                self.game.slide(side)
                
                price = self.calculatePrice()
                if price > bestPrice:
                    bestPrice = price
                    bestPriceSide = side
                
                self.game.pop()
            
            #take best possible action
            if bestPriceSide is not None:
                result = self.game.slide(bestPriceSide)
            else:
                result = self.playFallback()

    def playFallback(self):
        return self.game.slide( randint(0, 4) )
    
    def calculatePrice(self):
        return (self.game.statsScore - self.game.getPushedScore()) * self.PRICE_SCORE