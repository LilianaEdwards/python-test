import sys
import pygame
from 12_2 import Ship
from 12_2_setting import Settings
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,
         ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 255, 255)
    
    ship = Ship(screen)
    
    while True:
      #  for event in pygame.event.get():
     #       if event.type == pygame.QUIT:
     #           sys.exit()
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()
    
run_game()