import sys 

import pygame

from bullet import Bullets

from alien import Alien





def check_keydown_event(event,ship,ai_settings,screen,bullets) :
        if event.key == pygame.K_RIGHT :
            ship.moving_right = True
        elif event.key == pygame.K_q :
            sys.exit()
        elif event.key == pygame.K_LEFT :
            ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            fire_bullet(ai_settings,screen,ship,bullets)
        
        # elif event.key == pygame.K_UP :
        #     ship.moving_up = True
        # elif event.key == pygame.K_DOWN :
        #     ship.moving_down = True

def fire_bullet(ai_settings,screen,ship,bullets) :
    if len(bullets) < ai_settings.bullets_allowed :
        new_bullets = Bullets(ai_settings,screen,ship)
        bullets.add(new_bullets)

def check_keyup_event(event,ship) :
    if event.key == pygame.K_RIGHT :
        ship.moving_right = False
    elif event.key == pygame.K_LEFT :
        ship.moving_left = False
    # elif event.key == pygame.K_UP :
    #     ship.moving_up = False
    # elif event.key == pygame.K_DOWN :
    #     ship.moving_down = False

def check_events(ai_settings,screen,ship,bullets) :
    """Response to the key and mouse key"""

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()

        elif event.type == pygame.KEYDOWN :
            check_keydown_event(event,ship,ai_settings,screen,bullets)

        elif event.type == pygame.KEYUP :
            check_keyup_event(event,ship)

def update_bullets(bullets) :
        
    bullets.update()   

    for bullet in bullets.copy() :
        if bullet.rect.bottom <= 0 :
            bullets.remove(bullet)

def get_number_aliens_x(ai_settings,alien_width) :
    avaliable_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(avaliable_space_x / (2 * alien_width))
    return number_aliens_x

def get_nuber_rows(ai_settings,ship_height,alien_height) :
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)

    number_rows = int(available_space_y / (2 * alien_height)) 

    return number_rows
    
def create_alien(ai_settings,screen,aliens,alien_number,row_number) :
    alien = Alien(ai_settings,screen) 
    alien_width  = alien.rect.width  
    alien.x = alien_width +2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings,screen,aliens,ship) :
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_nuber_rows(ai_settings,ship.rect.height,alien.rect.height)

    for row_number in range(number_rows) :
        for alien_number in range(number_aliens_x) :
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

            
def update_screen(ai_settings,screen,ship,bullets,aliens) :
    """Change the screen and ai settings"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites() :
        bullet.draw_bullets()

    ship.blitme()
    # alien.blitme()
    aliens.draw(screen)

    pygame.display.flip() 