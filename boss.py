# boss.py
import pygame
import time
from pygame.sprite import Sprite
from bullet import BossBullet

pygame.mixer.init()



class Boss(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Завантаження звуків
        self.attack_sound = pygame.mixer.Sound('D:/Save/boss_attack.mp3')
        self.explosion_sound = pygame.mixer.Sound('D:/Save/boss_burst_louder.wav')
        
        # Завантаження зображень
        self.image = pygame.image.load('D:/Save/boss.jpg')  # основне зображення
        self.explosion_image = pygame.image.load('D:/Save/burst.png')  # вибух
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.midtop = self.screen_rect.midtop
        self.x = float(self.rect.x)

        self.health = 5
        self.alive = True
        self.direction = 1  # 1 = вправо, -1 = вліво
        self.moving = True
        self.last_attack_time = time.time()
        self.bullets = pygame.sprite.Group()

    def update(self):
        if not self.alive:
            return

        # Рух
        if self.moving:
            self.x += self.settings.boss_speed * self.direction
            self.rect.x = int(self.x)

            if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
                self.direction *= -1

        # Атака кожні 5 сек
        current_time = time.time()
        if current_time - self.last_attack_time > 3:
            self.attack()
            self.last_attack_time = current_time

        # Оновлення куль
        self.bullets.update()

    def attack(self):
        self.moving = False
        self.attack_sound.play()

        for i in range(10):  # 5 куль
            offset = i * 100 
            bullet = BossBullet(self.screen, self.rect.centerx + offset, self.rect.bottom)
            self.bullets.add(bullet)
        pygame.time.set_timer(pygame.USEREVENT + 1, 1000)  # через 1 сек знову рух

    def draw(self):
        if self.alive:
            self.screen.blit(self.image, self.rect)
            self.bullets.draw(self.screen)
            self.draw_health_bar()

    def draw_health_bar(self):
        health_ratio = self.health / 10
        bar_width = self.rect.width
        bar_height = 10
        fill_width = int(bar_width * health_ratio)
        bar_rect = pygame.Rect(self.rect.left, self.rect.top - 10, bar_width, bar_height)
        fill_rect = pygame.Rect(self.rect.left, self.rect.top - 10, fill_width, bar_height)
        pygame.draw.rect(self.screen, (255, 0, 0), bar_rect)
        pygame.draw.rect(self.screen, (0, 255, 0), fill_rect)

    def hit(self, damage):
        self.health -= damage
        self.direction *= -1.4
        if self.health <= 0:
            self.die()

    def die(self):
        self.alive = False
        self.explosion_sound.set_volume(0.3)  # Максимальна гучність
        self.explosion_sound.play()
        self.image = self.explosion_image
        pygame.time.set_timer(pygame.USEREVENT + 2, 1000)  # зникне через 1 сек
