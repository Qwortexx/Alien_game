class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.high_score = 0
        self.reset_stats()
        self.game_active = False
        self.game_over = False

    def reset_stats(self):
        self.ship_left = self.settings.ship_left
        self.score = 0
        self.game_over = False
        self.level = 1