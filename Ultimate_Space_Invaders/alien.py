import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Class to create a single alien in the fleet.'''
    
    def  __init__(self, space_game):
        super().__init__()
        self.screen = space_game.screen
        self.settings = space_game.settings
        #Load the alien image and set its rect attribute.
        self.image = pygame.image.load('alien_ship.png')
        self.rect = self.image.get_rect()
        
        #Start each new alien near the top left of the screen .
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
        
    def check_edges(self):
        '''This will return True if aliens hit the edges''' 
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True 
    def update(self):
        '''Changing the alien's position to right or left.'''
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x