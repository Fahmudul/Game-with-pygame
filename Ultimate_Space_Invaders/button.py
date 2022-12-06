import pygame.font

class Button:
    def __init__(self, space_game, msg) -> None:
        '''Initialize the button properties.'''
        self.screen = space_game.screen
        self.screen_rect = self.screen.get_rect()
        
        #Settings the dimension of the button and others
        self.width, self.height = 350, 50
        self.button_color = (51, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        #Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        #This message should be appears only the first time when someone wants to play the game.
        self._prep_msg(msg)
        
    def _prep_msg(self, msg):
        '''This will transform the text into an image and display it at the center of the screen.'''
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def create_button(self):
        #Draw button with a blank space and other properties.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)