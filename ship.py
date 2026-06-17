import pygame

class Ship() :
    """Initalize the images of the games"""

    def __init__(self,screen) :
        """Initlize the ship and set its starting position"""

        self.screen = screen

        #load  the ship images and get its rect
        self.images = pygame.image.load("images/ship2.jpg")
        self.images = pygame.transform.scale(self.images,(80,90))
        self.rect = self.images.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at te bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self) :
        """Draw the ship at its currunt location"""
        self.screen.blit(self.images,self.rect)
    
    