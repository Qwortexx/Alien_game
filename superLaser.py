import pygame
import time

class SuperLaser:

    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.ship = ai_game.ship

        self.frames = []
        for i in range(1,6):
            try:
                image = pygame.image.load(f"D:/Save/laser{i}.png").convert_alpha()
                image = pygame.transform.scale(image, (50, 300))
                self.frames.append(image)

            except:
                if len(self.frames)>0:
                    self.frames.append(self.frames[0])
                else:
                    image = pygame.image.load("D:/Save/laser3.png").convert_alpha()
                    image = pygame.transform.scale(image, (50, 300))
                    self.frames.append(image)

        self.current_frame = 0
        self.frame_time = 0
        self.frame_delay = 0.5


#        self.image = pygame.transform.rotate(smaller_image, 90)

        self.rect = self.frames[0].get_rect()

        self.rect.centerx = self.ship.rect.centerx
        self.rect.bottom = self.ship.rect.top

        self.active = True

        self.activation_time = 0
        self.duration = 5

    def updateLaser(self, current_time):
        self.rect.centerx = self.ship.rect.centerx
        self.rect.bottom = self.ship.rect.top

        if current_time - self.frame_time >= self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.frame_time = current_time

        if self.active and current_time - self.activation_time >= self.duration:
            self.active = False

    def drawLaser(self):
        if self.active:
            self.screen.blit(self.frames[self.current_frame], self.rect)