import sys
import pygame
from class_Settings import settings
from class_Space_ship import Space_Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_statistic import Game_Info
from button import Button
from score_board import ScoreBoard


class Space_Invaders:
    '''Over all properties and others game materials'''

    def __init__(self) -> None:
        '''Initialize the game's Window'''
        pygame.init()
        self.settings = settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.width = self.screen.get_rect().width
        self.settings.height = self.screen.get_rect().height
        self.bG_color = self.settings.bg_color
        self.back_ground = pygame.transform.scale(
            pygame.image.load("space_image.jpg"), (self.settings.width, self.settings.height))
        self.game_window = pygame.display.set_caption("Space Invaders")
        self.stats = Game_Info(self)
        # Create an instance to store game statistic
        self.sb = ScoreBoard(self)
        self.game_icon = pygame.display.set_icon(
            pygame.image.load("game_icon_2.png"))
        self.ship = Space_Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # Draw the play button
        self.play_button = Button(self, "Play Space Invaders!")

    '''Start the main game functionalities'''

    def play_game(self):
        '''Start the game'''

        Game_On = True
        # Wathcing all keyboard and mouse movement
        while Game_On:
            self.check_events()
            if self.stats._game_active:
                self.ship.update()
                self.bullets.update()
                self._update_bullet()
                self._update_alien()

            self.update_screen()

    def check_events(self):
        '''Check to see player keypressed mouse or keyboard'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:

                # Move the ship to the right or left
                self.check_keydown_status(event)

            elif event.type == pygame.KEYUP:
                self.check_keyup_status(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _create_fleet(self):
        '''Create the fleet of aliens.'''
        # Drawing aliens
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Calculate the number of rows of aliens that can fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        # Creating the first row of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                # Draw an alien and place it in the row.
                self._create_alien(alien_number, row_number)

    def _check_play_button(self, mouse_pos):
        '''This will start the game if the player cilck on the play button.'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats._game_active:
            self.settings.initialize_automatic_speed()
            self.stats.reset_all_stat()
            self.stats._game_active = True

            self.sb._draw_score()
            self.sb.draw_level()
            # self.sb._prep_ship()

            self.aliens.empty()
            self.bullets.empty() 
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)

    def _check_fleet_edges(self):
        '''This will happen if any aliens have reached the edges.'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''Drop the entire alien and the fleets direction.'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_that_hits_by_alien(self):
        '''This will respond to the ship if hit by the alien.'''

        if self.stats.ship_left > 0:
            # Decrement ships left.
            self.stats.ship_left -= 1
            self.sb._prep_ship()
            

            # Get rid of any existing alien and space ship.
            self.aliens.empty()
            self.bullets.empty()

            # Creating new aliens and center the space ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause the game for a sec
            sleep(0.5)
        else:
            self.stats._game_active = False
            pygame.mouse.set_visible(True)

    def _update_alien(self):
        '''Update the positions of aliens in the screen.'''
        self._check_fleet_edges()
        self.aliens.update()

        # Looking for ship and alien collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_that_hits_by_alien()

        # Checking if any aliens reached at the bottom of the screen.
        self._checking_alien_reached_at_bottom()

    def _checking_alien_reached_at_bottom(self):
        '''Checking if any aliens already reached at the bottom of the screen.'''
        screen_rect = self.screen.get_rect()
        for aliens in self.aliens.sprites():
            if aliens.rect.bottom >= screen_rect.bottom:
                # Treat this as the same as ship_hit method.
                self._ship_that_hits_by_alien()
                break

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_bullet(self):
        '''Update position of bullets and remove the old bullets.'''
        self.bullets.update()
        # Remove the old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_collided_with_alien()

        # Check for any bullets that collide each other.
        # If it is, get rid of the bullet and the alien. From the screen.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

    def _check_bullet_collided_with_alien(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_point * len(aliens)
            
            self.sb._draw_score()
            self.sb.check_high_score()
        if not self.aliens:
            # Destroy existing bullets and create new alien.q
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            
            self.stats.level += 1
            self.sb.draw_level()

    def check_keydown_status(self, event):
        '''Respond to keypress'''
        if event.key == pygame.K_RIGHT:
            self.ship.change_position_flag_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.change_position_flag_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def check_keyup_status(self, event):
        '''Respond to key relase'''
        if event.key == pygame.K_RIGHT:
            self.ship.change_position_flag_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.change_position_flag_left = False

    def _fire_bullet(self):
        '''Create a new bullet and add it to the bullets group.'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def update_screen(self):
        '''Update the image on the game screen, and update everything '''
        self.screen.fill(self.bG_color)
        self.screen.blit(self.back_ground, (0, 0))
        self.ship.bilt_me()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.update()
        self.aliens.draw(self.screen)
        self.sb.show_score()
        if not self.stats._game_active:
            self.play_button.create_button()
        pygame.display.flip()


if __name__ == "__main__":
    space_game = Space_Invaders()
    space_game.play_game()
