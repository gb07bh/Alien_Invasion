import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_funtion as gf
from game_stats import GameStats
from alien import Alien
from button import Button
from scoreboard import Scoreboard
import sound_effects as se
   
#Main Program        
def game():
    #create screen object
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode(
        (ai_settings.screen_width , ai_settings.screen_height)
        )
    #Making a Ship
    ship = Ship(ai_settings,screen)
    alien = Alien(ai_settings,screen)
    bullets = Group()
    aliens = Group()
  
    

    #Creating alien Fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)
    

    pygame.display.set_caption("ALIEN ATTACK")
    

    #Stats
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    play_button = Button(ai_settings, screen, 'PLAY')

    #background color (little grey)
    while True:
        gf.check_events(ai_settings, screen,stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
           ship.update()
           gf.update_bullets(ai_settings, screen, stats, sb, 
             ship, aliens, bullets)      
           gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
           
        gf.update_screen(ai_settings, screen ,stats, sb, ship,
         aliens, bullets, play_button)
                
game() 
