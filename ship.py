import pygame

class Ship() :
    """Initalize the images of the games"""

    def __init__(self,screen) :
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

    def update(self) :
        if self.moving_right :
            self.rect.centerx += 1 

        elif self.moving_left :
            self.rect.centerx -= 1

    def blitme(self) :
        """Draw the ship at its currunt location"""
        self.screen.blit(self.images,self.rect)


    