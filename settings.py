class Settings:
    def __init__(self):

        self.screen_width = 1600
        self.screen_height = 1000
        self.bg_color = (230,230,230)
        self.ship_speed = 10.0
        self.bullet_speed = 10.0
        self.bullet_height = 17
        self.bullet_width = 5
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 1.5

        self.speedup_scale = 1.6


        self.boss_attack_delay = 3 
        
        self.alien_moving = 1


        self.spawn_interval = 8
        self.ship_left = 3

        self.alien_points = 50
        self.boss_speed = 3.0
        self.base_ship_speed = 10.0