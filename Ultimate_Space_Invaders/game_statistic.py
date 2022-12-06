class Game_Info:
    '''This class will do all the game info for this game.'''
    
    def __init__(self, ship_game) -> None:
        '''Initialize game's statistic.'''
        self.settings = ship_game.settings
        self.reset_all_stat()
        #Start the game in an inactive 
        self._game_active = False
        #High score
        self.high_score = 0
        
    
    def reset_all_stat(self):
        '''This method will change during the players playing the game.'''
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        