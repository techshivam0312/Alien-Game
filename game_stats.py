class GaameStats() :
    def __init__(self,ai_setings) :
        self.ai_settings =  ai_setings
        self.reset_stats()
        self.game_active  = True

    def reset_stats(self) :
        self.ship_left = self.ai_settings.ship_limit