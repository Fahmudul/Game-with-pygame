import pygame
'''Settings of the game and others'''
class settings:
    def __init__(self) -> None:
        # Initialize the game screen
        self.height = 1200
        self.width = 800
        self.bg_color = (100, 100, 100)
        # Bullet Settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (220, 220, 220)
        self.bullets_allowed = 3
        #Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.ship_limit = 3
        # fleet coordinate change 1 represent right ; -1 represent left
        self.fleet_direction = 1
        
        #Game speeds up
        self.speed_up_scale = 1.1
        
        self.initialize_automatic_speed()
        
    def initialize_automatic_speed(self):
        '''Initialize the game settings which will change depending on the player's level.'''
        
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        
        self.fleet_direction = 1
        
        #Score
        self.alien_point = 1
        
    def increase_speed(self):
        '''Increase the game speed.'''
        self.ship_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale