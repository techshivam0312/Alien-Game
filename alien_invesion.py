import pygame

from settings import Settings

from ship import Ship

import game_functions as gf

from pygame.sprite import Group

from alien import Alien

def run_game() :
    """Initilize the game and creates a screen objects """
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    ship = Ship(ai_settings,screen)

    bullets = Group()

    aliens = Alien(ai_settings,screen)

    aliens = Group()

    gf.create_fleet(ai_settings, screen, aliens, ship)


    while True :
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,bullets,aliens)


run_game()
