import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load("C:/Python/alien_gametiny_ship14.bmp")
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.spawn_interval = 10

        self.x = float(self.rect.x)