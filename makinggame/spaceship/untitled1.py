import pygame
from settings import Settings
from ship import Ship



import sys
import pygame
def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ship = Ship(screen)
    ai_settings = Settings()
    screen = pygame.display.set_mode(

        (ai_settings.screen_width, ai_settings.screen_height))
    
    
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    # Set the background color. u 
    
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Make the most recently drawn screen visible. c
        
        screen.fill(ai_settings.bg_color)
        pygame.display.flip()
run_game()


