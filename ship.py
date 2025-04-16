import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        super().__init__()


        self.image = pygame.image.load('D:/Save/Ship6.bmp')
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Оновлення координат
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """Спавнить корабель у центрі екрану після зіткнення."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.settings.screen_width / 2)
        self.y = float(self.settings.screen_height / 2)

