import pygame
import sys
def run_game() :
    #Initialize game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("alien Invasion")
    #Set the gackground color
    screen.fill((255,0,0))
    #Start the main loop for the game.
    while True :
        #Watch for keyboard and mouse events
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                sys.exit()
        #Make the most recently drawn screen visible
        pygame.display.flip()
run_game()
