from random import randint
                            
class RandomStrategy:
    """
    RandomStrategy for Game 2048 
    """
    
    game = None
    
    def __init__(self, game):
        self.game = game
    
    def play(self):
        while self.game.slide( randint(0, 3) ) != 2:
            pass