import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
     
        self.text_color = (255, 255, 255)
        self.sb_color = (38, 9, 61)
        self.font = pygame.font.SysFont(None, 48)

        self.ai_game = ai_game

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_speed()
        self.prep_labels()
        self.prep_health()

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
        self.score_label_rect.right = self.score_rect.left - 50
        self.score_label_rect.top = self.score_rect.top

        # Мітка для рекорду
        self.high_score_label = self.font.render("Record:", True, self.text_color, self.sb_color)
        self.high_score_label_rect = self.high_score_label.get_rect()
        self.high_score_label_rect.right = self.high_score_rect.left - 50
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

        # Швидкість
        self.screen.blit(self.speed_label, self.speed_label_rect)
        self.screen.blit(self.speed_image, self.speed_rect)

        self.ships.draw(self.screen)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_health(self):
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    
    def prep_speed(self):
        # Відображення поточної швидкості корабля
        speed_str = str(round(self.settings.ship_speed, 2))
        self.speed_image = self.font.render(speed_str, True, self.text_color, self.sb_color)

        self.speed_rect = self.speed_image.get_rect()
        self.speed_rect.right = self.level_rect.right
        self.speed_rect.top = self.level_rect.bottom + 10

        # Мітка для швидкості
        self.speed_label = self.font.render("Speed: ", True, self.text_color, self.sb_color)
        self.speed_label_rect = self.speed_label.get_rect()
        self.speed_label_rect.right = self.speed_rect.left - 10
        self.speed_label_rect.top = self.speed_rect.top 