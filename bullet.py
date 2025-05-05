import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):


     def __init__(self, ai_game):
        super().__init__() #super для належного успадкування Sprite
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('D:/Save/Ship6.bmp')
               
        # Завантаження зображення кулі
        self.image = pygame.image.load("C:/Python/alien_game/bullet.png").convert_alpha()  # convert_alpha() для прозорості
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.scaled_image = pygame.transform.scale(self.image, (50,100))
        self.rect = self.scaled_image.get_rect()
        x, y = ai_game.ship.rect.midtop
        self.rect.midtop = (x, y - 50)
        self.y = float(self.rect.y)

     def update(self):
         self.y -= self.settings.bullet_speed
         self.rect.y = self.y

     def draw_bullet(self):
        self.screen.blit(self.scaled_image, self.rect)
