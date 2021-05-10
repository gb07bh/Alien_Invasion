import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #To represent alien in the fleet(Single)


    def __init__(self, ai_settings, screen):
        #initializing Alien and its position on screen
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load image of alien ship
        self.image =pygame.image.load('Images/ufo1.png')
        self.rect = self.image.get_rect()

        #placing new  alien at the top left corner of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #See alien's position
        self.x = float(self.rect.x)

      
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        #Moving Alien to right
        self.x += (self.ai_settings.alien_speed_factor *
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        #Alien on screen
        self.screen.blitme(self.image, self.rect)
        
    
