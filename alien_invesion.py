import pygame

from settings import Settings

from ship import Ship

import game_functions as gf

from pygame.sprite import Group

from alien import Alien

from game_stats import GaameStats

from button import Button

from scoreboard import ScoreBoard

def run_game() :
    """Initilize the game and creates a screen objects """
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    ship = Ship(ai_settings,screen)

    bullets = Group()

    aliens = Alien(ai_settings,screen)

    aliens = Group()

    stats = GaameStats(ai_settings)

    gf.create_fleet(ai_settings, screen, aliens, ship)

    play_button = Button(ai_settings,screen,"Play")

    sb= ScoreBoard(ai_settings,screen,stats)


    while True :
        gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets,aliens,ai_settings,screen,ship,stats,sb)
            gf.update_aliens(ai_settings,ship,aliens,bullets,screen,stats)
        gf.update_screen(ai_settings,screen,stats,sb, ship,bullets,aliens,play_button)


run_game()
