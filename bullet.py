import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #Class to manage bullets fired from ship
    def __init__(self,ai_settings,screen,ship):
        #Creating bullets object at ships position
        super(Bullet,self).__init__()
        self.screen=screen
        
        #Create bullet at rect(0,0) and then set correct position.
        self.rect  =  pygame.Rect(0,0,
          ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx  =  ship.rect.centerx
        self.rect.top  =  ship.rect.top

        #Store Bullets position as decimal value
        self.y  =  float(self.rect.y)

        self.color  =  ai_settings.bullet_color
        self.speed_factor  =  ai_settings.bullet_speed_factor
        
    def update(self):
        #Moving bullet up the screen
        #Updating Decimal position of bullet
        self.y -= self.speed_factor
        #Update the rect  position
        self.rect.y=self.y

    def draw_bullet(self): 
        #Drawing bullet to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)

