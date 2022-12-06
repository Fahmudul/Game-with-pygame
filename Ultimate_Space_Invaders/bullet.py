import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''This class is used to manage bullets fired from the ships.'''
    def __init__(self,space_game) -> None:
        '''Creating a bullet object at the position of the ship. '''
        super().__init__()
        self.screen = space_game.screen
        self.settings = space_game.settings
        self.color = self.settings.bullet_color
        
        #Creating a bullet rect at (0, 0) by default and then we will change it's position
        
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = space_game.ship.rect.midtop
        
        # Storing the bullet's porition as a decimal value.
        self.y = float(self.rect.y)
    def update(self):
        '''fire the bullet from the ship.'''
        #update the decimal postion of the bullet. 
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
        
    def draw_bullet(self):
        '''Draw the bullet on the game window.'''
        pygame.draw.rect(self.screen, self.color, self.rect)
        