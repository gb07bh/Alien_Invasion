import sys
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        super(Ship,self).__init__()
        self.screen    =    screen
        self.ai_settings    =    ai_settings

        #Starting new ship from bottom
        self.image = pygame.image.load('Images/rckt.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect() #rect( for rectangles)
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
       

        #Store value(decimal)  for ship's center
        self.centerx = float(self.rect.centerx)
        self.centy = float(self.rect.centery)
        
        #Movement Flags
        self.moving_right = False #Movement Flag for right
        self.moving_left = False #Movement Flag for left
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        #updating positions according to flags.
         #Updating ship's center value and not rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx  +=  self.ai_settings.ship_speed_factor
        
        if self.moving_left and self.rect.left > 0:
            self.centerx    -=   self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centy -= self.ai_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom :
            self.centy += self.ai_settings.ship_speed_factor

              
      #Update rect from center
        self.rect.centerx = self.centerx
        
        self.rect.centery = self.centy

    
    
        
    def blitme(self):
        self.screen.blit(self.image,self.rect) #drawing ship at current location

    def center_ship(self):
        # ship at center
        self.centerx = self.screen_rect.centerx
        self.centy = self.screen_rect.bottom - 29
        
        
       
        

        
        
        