import pygame

class Ship() :
    """Initalize the images of the games"""

    def __init__(self,ai_settings,screen) :
        """Initlize the ship and set its starting position"""

        self.screen = screen
        
        self.images = pygame.image.load("images/Thor.bmp")
        self.images = pygame.transform.scale(self.images,(80,90))
        self.rect = self.images.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.ai_settings = ai_settings

        self.centerx = float(self.rect.centerx)
        # self.centery = float(self.rect.centery)

    def update(self) :
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.centerx += self.ai_settings.ship_speed

        elif self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed

        # elif self.moving_up and self.rect.top > 0 :
        #     self.centery -= self.ai_settings.ship_speed

        # elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
        #     self.centery += self.ai_settings.ship_speed

        self.rect.centerx = self.centerx
        # self.rect.centery = self.centery

            
    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx


    def blitme(self) :
        """Draw the ship at its currunt location"""
        self.screen.blit(self.images,self.rect)
    
    