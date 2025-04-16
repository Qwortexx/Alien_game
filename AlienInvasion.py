import pygame
import sys
import settings
import time
import random
from bullet import Bullet
from ship import Ship
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
#from ship02 import ship02

pygame.init()

pygame.mixer.music.load('D:/Save/background_music.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

shot_sound = pygame.mixer.Sound('D:/Save/short_shot_sound.wav')
hit_sound = pygame.mixer.Sound('D:/Save/hit_sound.wav')

class AlienInvasion:


    def __init__(self):
        pygame.init()
        self.settings = settings.Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.bg_image = pygame.image.load('D:/Save/background.bmp')
        self.bg_image = pygame.transform.scale(self.bg_image, (self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.last_spawn_time = time.time()
        #self.ship02 = ship02(self)
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.play_button = Button(self,"Play")

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self.bullets.update()
                self._update_bullet()
                self._update_alien()
                self._update_alien_position()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get(): # перевірка чи кнопку нажато чи ні
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event): # Якщо нажали то залежно від кнокпи буде змінюватись змінна на True і буде рух корабля
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            shot_sound.play()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event): # Якщо відпустили
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):# максимальна кількість пуль 5, перевірка чи не більше 5 якщо більше 5 то стріляти неможливо
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self): # якщо куля за екраном то вона видаляться
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))
        # якщо куля влучила в прибульця то вони видаляються
        collections = pygame.sprite.groupcollide(self.bullets, self.aliens, True,True)
        if collections:
            hit_sound.play()
            for aliens in collections.values():
                # Додаємо очки за кожного збитого прибульця
                self.stats.score += self.settings.alien_points * len(aliens)
            # Оновлюємо зображення рахунку
            self.sb.prep_score()
            self.sb.check_high_score()
            self.sb.prep_health()


    def _update_screen(self):  # Відображення
        self.screen.blit(self.bg_image, (0, 0))

        if self.stats.game_active:
            self.ship.blitme()
            self.aliens.draw(self.screen)
            self.sb.show_score()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
        else:
            if self.stats.game_over:
               self._show_game_over()
            self.play_button.draw_button()

        pygame.display.flip()

    def _show_game_over(self):
        font = pygame.font.SysFont(None, 72)
        text = font.render("Game Over!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.settings.screen_width // 2, self.settings.screen_height // 2.5))
        self.screen.blit(text, text_rect)

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # Обчислення максимальної кількості інопланетян у ряді
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        max_aliens_in_wave = number_aliens_x // 4
        random_positions = self._get_unique_positions(number_aliens_x, max_aliens_in_wave, alien_width)

        for alien_number in random_positions:
            self._create_alien(alien_number, alien_width, alien_height)

    def _get_unique_positions(self, number_aliens_x, max_aliens, alien_width):
        existing_positions = {alien.rect.x for alien in self.aliens}  # Координати вже існуючих інопланетян
        possible_positions = [i for i in range(number_aliens_x) if
                              (alien_width + 2 * alien_width * i) not in existing_positions]

        # Вибираємо випадкові позиції серед вільних
        return random.sample(possible_positions, min(max_aliens, len(possible_positions)))

    def _create_alien(self, alien_number, alien_width, alien_height):
        alien = Alien(self)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height
        self.aliens.add(alien)


    def _update_alien(self):
        self.aliens.update()
        for alien in self.aliens.copy():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break
            elif pygame.sprite.spritecollideany(self.ship, self.aliens):
                print("Ship hit!!!")
                self._ship_hit()
        print(len(self.aliens))

    def _update_alien_position(self):
        current_time = time.time()

        # Оновлення позицій інопланетян (рух вниз)
        for alien in self.aliens.sprites():
            alien.rect.y += 1

        # Перевірка: спавнимо нову хвилю тільки якщо всі прибульці знищені
        if not self.aliens and (current_time - self.last_spawn_time >= self.settings.spawn_interval):
            self.stats.level += 1
            self.sb.prep_level()

            self._create_fleet()
            self.last_spawn_time = current_time

    def _ship_hit(self):
        self.stats.ship_left -= 1            
        self.sb.prep_health()

        if self.stats.ship_left > 0:
            self.aliens.empty()
            self.bullets.empty()

            self.ship.center_ship()
            self._create_fleet()


            sleep(1)
        else:
            self.stats.game_active = False
            self.stats.game_over = True
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break
    def _check_play_button(self,mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:

            self.stats.reset_stats()
            self.stats.game_active = True
            self.stats.game_over = False

            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_health()


            self.aliens.empty()
            self.bullets.empty()


            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()