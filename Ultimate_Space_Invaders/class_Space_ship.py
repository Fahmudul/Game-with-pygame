import pygame
from pygame.sprite import Sprite

class Space_Ship(Sprite):
    '''A class to manage the ship'''

    def __init__(self, space_Ship) -> None:
        super().__init__()
        self.screen = space_Ship.screen
        self.screen_rect = space_Ship.screen.get_rect()

        # Load the ship image
        self.ship_image = pygame.image.load("spaceship.png")
        self.rect = self.ship_image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        # Change position flag
        self.change_position_flag_right = False
        self.change_position_flag_left = False

    def center_ship(self):
        '''This method will center the ships after a collision with an alien.'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        '''Update the ship's position according to the flag.'''
        if self.change_position_flag_right and self.rect.right < self.screen_rect.right:
            self.x += 5.5
        elif self.change_position_flag_left and self.rect.left > 0:
            self.x -= 5.5
        self.rect.x = self.x

    def bilt_me(self):
        '''Draw the ship at its current position.'''
        self.screen.blit(self.ship_image, self.rect)
