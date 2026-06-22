import sys 

from time import sleep

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

def check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets,sb) :
    """Response to the key and mouse key"""

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN :
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y,sb)

        elif event.type == pygame.KEYDOWN :
            check_keydown_event(event,ship,ai_settings,screen,bullets)

        elif event.type == pygame.KEYUP :
            check_keyup_event(event,ship)

def check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y,sb):

    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active :

        pygame.mouse.set_visible(False)

        stats.reset_stats()
        stats.game_active = True

        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings,screen,aliens,ship)

def update_bullets(bullets,aliens,ai_settings,screen,ship,stats,sb) :

    bullets.update()   

    for bullet in bullets.copy() :
        if bullet.rect.bottom <= 0 :
            bullets.remove(bullet)
    check_bullets_alien_collision(bullets,aliens,ai_settings,screen,ship,stats,sb)

def check_bullets_alien_collision(bullets,aliens,ai_settings,screen,ship,stats,sb) :

    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

    if collisions :
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
        sb.prep_score()
    check_high_score(stats,sb)

    if len(aliens) == 0 :
        bullets.empty()
        # create_fleet(ai_settings,screen,aliens,ship)
        stats.game_active = False
        pygame.mouse.set_visible(True)
        stats.level += 1 
        sb.prep_level()


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

def check_fleet_edges(ai_settings,aliens) :
    for alien in aliens.sprites():
        if alien.check_edges() :
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
         alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens,bullets):

    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if a ship got hit.
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
            break

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb) :
    if stats.ship_left > 0 :
        stats.ship_left -= 1 

        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings,screen,aliens,ship)

        ship.center_ship()
        
        sleep(0.5)
    else :
        stats.game_active = False
        pygame.mouse.set_visible(True)

def update_aliens(ai_settings,ship,aliens,bullets,screen,stats,sb) :

    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship,aliens) :
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb)

    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_high_score(stats, sb):

    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

            
def update_screen(ai_settings,screen,stats,sb,ship,bullets,aliens,play_button) :
    """Change the screen and ai settings"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites() :
        bullet.draw_bullets()

    ship.blitme()
    # alien.blitme()
    aliens.draw(screen)
    sb.show_score()

    if not stats.game_active :
        play_button.draw_button()

    pygame.display.flip() 