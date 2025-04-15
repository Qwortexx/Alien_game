class Settings:
    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed = 5
        self.bullet_speed = 3.0
        self.bullet_height = 17
        self.bullet_width = 5
        self.bullet_color = (255, 0, 0)
        self.bullet_allowed = 5

        self.speedup_scale = 1.1


        self.spawn_interval = 10
        self.ship_left = 3

        self.alien_points = 50