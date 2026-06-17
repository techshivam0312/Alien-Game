import sys 

import pygame

def check_function() :
    """Response to the key and mouse key"""

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()
        

def update_screen(ai_settings,screen,ship) :
    """Change the screen and ai settings"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    pygame.display.flip() 