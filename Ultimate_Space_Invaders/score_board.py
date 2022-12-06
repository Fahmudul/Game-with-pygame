import pygame.font
from pygame.sprite import Group
from class_Space_ship import Space_Ship
class ScoreBoard:
    '''A class to create a report of the game's scoring information.'''
    def __init__(self, ship_game) -> None:
        self.ship_game = ship_game
        self.screen = ship_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ship_game.settings
        self.stats = ship_game.stats
        
        #Font information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        #Set the score image
        self._draw_score()
        self._draw_high_score()
        self.draw_level()
        # self._prep_ship()
    def _draw_score(self):
        '''Transform the score into a image.'''
        score_str = str(self.stats.score)
        self.score_image = self.font.render("Score : "+score_str, True, self.text_color, self.settings.bg_color)
        
        #Display the score at tha top right corner of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    
    def _draw_high_score(self):
        '''Transform the high score into an image.'''
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score) 
        self.high_score_image = self.font.render("High Score : "+high_score_str, True, self.text_color, self.settings.bg_color)
    
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    def check_high_score(self):
        '''Check if there a high score occurs.'''
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self._draw_high_score()
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # self.ships.draw(self.screen)
        
    def draw_level(self):
        '''Transform the level into an image.'''
        level_str = str(self.stats.level)
        self.level_image = self.font.render('Level : '+level_str, True, self.text_color, self.settings.bg_color)
        
        #Positioning the co ordinate of the level image.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    # def _prep_ship(self):
    #     '''This will show how many ships are remaining.'''
    #     self.ships = Group()
    #     for ship_number in range(self.stats.ship_left):
    #         ship = Space_Ship(self.ship_game)
    #         ship.rect.x = 10 + ship_number * ship.rect.width
    #         ship.rect.y = 10
    #         self.ships.add(ship)