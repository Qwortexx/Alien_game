import pygame
import time

class SuperLaser:

    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.ship = ai_game.ship

        self.image = pygame.image.load("C:/Users/PK/Downloads/SuperLaser.bmp")

        smaller_image = pygame.transform.scale(self.image, (350, 100))

        self.image = pygame.transform.rotate(smaller_image, 90)

        self.rect = self.image.get_rect()

        self.rect.centerx = self.ship.rect.centerx
        self.rect.bottom = self.ship.rect.top

        self.active = True

        self.activation_time = 0
        self.duration = 5

    def updateLaser(self, current_time):
        self.rect.centerx = self.ship.rect.centerx
        self.rect.bottom = self.ship.rect.top

        if self.active and current_time - self.activation_time >= self.duration:
            self.active = False

    def drawLaser(self):
        if self.active:
            self.screen.blit(self.image, self.rect)