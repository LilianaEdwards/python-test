import pygame
import sys
from settings import Settings
def run_game() :
    #Initialize game,settings and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #Start the main loop for the game.
    while True :
        #Watch for keyboard and mouse events
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                sys.exit()
        #Redraw the screen during eacn pass through the loop
        screen.fill(ai_settings.bg_color)
        #Make the most recently drawn screen visible
        pygame.display.flip()
run_game()
