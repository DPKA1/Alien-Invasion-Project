import sys
import pygame
from settings3 import Settings3
from game_stats3 import GameStats
from ship3 import Ship
from alien3 import Alien
import game_functions3 as gf
from pygame.sprite import Group
from button import Button
from scoreboard import Scoreboard

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings3()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

# Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

# Create an instance to store game statistics and scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship.
    ship = Ship(ai_settings, screen)

    #Make a group to store bullets in.
    bullets = Group()
    aliens = Group()

   

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

 # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
         #gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)
        if stats.game_active:
                ship.update()
                gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
                gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        #gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()



       
   




