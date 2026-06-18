import pygame

from settings import Settings

from ship import Ship

import game_functions as gf


def run_game() :
    """Initilize the game and creates a screen objects"""
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    ship = Ship(screen)


    while True :
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)


run_game()