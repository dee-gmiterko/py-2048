#!/usr/bin/env python
# coding=utf-8

from SimpleStrategy import SimpleStrategy
from random import randint

                            
class PredictableStrategy(SimpleStrategy):
    """
    PredictableStrategy for Game 2048 
    """

    PREDICTION_LEVELS = 2
    PRICE_TILE = 0.5
    PRICE_PREDICTED = 0.1

    def playFallback(self):
        result = self.game.slide(0)
        if result == 1:
            return self.game.slide(randint(0, 4))
        else:
            return result
    
#    def calculatePrice(self, originalScore):
#        
#        price = (self.game.statsScore - originalScore) * self.PRICE_SCORE
#        
#        for predictionLevel in range(1, self.PREDICTION_LEVELS + 1):
#            for x in range(0, self.game.SIZE):
#                for y in range(0, self.game.SIZE):
#                    tilesPrice = self.calculateTilePrice(x, y) * self.PRICE_TILE
#                    price += tilesPrice * self.PRICE_PREDICTED * predictionLevel;
#        return price

    def calculatePrice(self):
#        print 21*'-'
#        print 'START CALCUALTE PRICE'
#        print 21*'-'
        
        return self.calculatePriceLevel(1)
    
#        print 21*'-'
#        print 'END CALCUALTE PRICE'
#        print 21*'-'

    def calculatePriceLevel(self, predictionLevel):
        
        price = (self.game.statsScore - self.game.getPushedScore()) * self.PRICE_SCORE

        if predictionLevel <= self.PREDICTION_LEVELS:
           
            for side in range(0, 4):

                self.game.push()

                self.game.slide(side)

                nextLevelPrice = self.calculatePriceLevel(predictionLevel + 1)
                price += nextLevelPrice * (self.PRICE_PREDICTED ** predictionLevel)

                self.game.pop()
        
        return price
