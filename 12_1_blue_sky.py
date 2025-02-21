import sys
import pygame
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 255, 255)

    while True:
        screen.fill(bg_color)
        pygame.display.flip()
    
run_game()
