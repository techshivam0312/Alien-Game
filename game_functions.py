import sys 

import pygame

from bullet import Bullets





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

            
def update_screen(ai_settings,screen,ship,bullets,alien) :
    """Change the screen and ai settings"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    alien.blitme()
    for bullet in bullets.sprites() :
        bullet.draw_bullets()

    pygame.display.flip() 