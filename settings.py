import sys
import pygame

class Settings():
    def __init__(self):
      self.screen_width = 1200  
      self.screen_height = 800
      self.bg_color = (38,45,65)
    
      # Ship Settings
       
      self.ship_limit = 3 #player lives
        
      # Bullet Settings
      
      self.bullet_width = 3
      self.bullet_height = 10
      self.bullet_color = (255,0,0)
      self.bullets_allowed = 3

      #Alien Settings
        
      self.fleet_drop_speed = 10
        
      self.speedup_scale = 1.1
      self.score_scale = 1.5

      self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):

      
      self.ship_speed_factor = 1.5
      self.alien_speed_factor = 1
      self.bullet_speed_factor = 3
      
      self.alien_score = 50
      self.fleet_direction = 1

    def increase_speed(self):
      self.ship_speed_factor *= self.speedup_scale
      self.alien_speed_factor *= self.speedup_scale
      self.bullet_speed_factor *= self.speedup_scale

      self.alien_score = int(self.alien_score * self.score_scale)
      print(self.alien_score)