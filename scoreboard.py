import pygame.font


class Scoreboard:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (255, 255, 255)
        self.sb_color = (38, 9, 61)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_labels()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.sb_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score_str = str(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.sb_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.sb_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_labels(self):
        # Мітка для поточного рахунку
        self.score_label = self.font.render("Score:", True, self.text_color, self.sb_color)
        self.score_label_rect = self.score_label.get_rect()
        self.score_label_rect.right = self.score_rect.left - 10
        self.score_label_rect.top = self.score_rect.top

        # Мітка для рекорду
        self.high_score_label = self.font.render("Record:", True, self.text_color, self.sb_color)
        self.high_score_label_rect = self.high_score_label.get_rect()
        self.high_score_label_rect.right = self.high_score_rect.left - 10
        self.high_score_label_rect.top = self.high_score_rect.top

        # Мітка для рівня
        self.level_label = self.font.render("Level:", True, self.text_color, self.sb_color)
        self.level_label_rect = self.level_label.get_rect()
        self.level_label_rect.right = self.level_rect.left - 10
        self.level_label_rect.top = self.level_rect.top

    def show_score(self):
        # Поточний рахунок
        self.screen.blit(self.score_label, self.score_label_rect)
        self.screen.blit(self.score_image, self.score_rect)

        # Рекорд
        self.screen.blit(self.high_score_label, self.high_score_label_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

        # Рівень
        self.screen.blit(self.level_label, self.level_label_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()