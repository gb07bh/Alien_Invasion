class GameStats():
    #Tracking stats for alien invasion :)
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.high_score = 0
        

        #Starting in an inactive state
        self.game_active = False




    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
     