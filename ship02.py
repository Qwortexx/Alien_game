import pygame


class ship02:

    def __init__(self,ai_game2):
        self.screen2 = ai_game2.screen
        self.screen2_rect = ai_game2.screen.get_rect()

        self.image = pygame.image.load('D:/Save/tiny_ship14.bmp')
        self.rect = self.image.get_rect()
        self.rect.midtop = self.screen2_rect.midtop

    def blitme(self):
            self.screen2.blit(self.image, self.rect)
