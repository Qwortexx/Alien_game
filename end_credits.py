import pygame


class EndCredit:

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = self.screen_rect.width, self.screen_rect.height

        self.title_font = pygame.font.SysFont('arial', 68, bold=True)
        self.text_font = pygame.font.SysFont('arial', 36)

        self.yellow = (255, 255, 0)
        self.white = (255, 255, 255)
        self.blue = (0, 100, 255)

        self.title_text = "Victory!"
        self.credits = [
            "Congratulations! You have saved the galaxy from invasion!",
            "",
            "The Space Defenders thank you for your bravery",
            "and dedication to the cause of peace in the Universe.",
            "",
            "Thanks to your efforts, the threat has been eliminated,",
            "and the planets of our system can rest easy.",
            "",
            "But stay vigilant, for evil never sleeps...",
            "",
            "Until the next adventure, space hero!",
            "",
            "Developers: Qwortex, Danilo ",
            "Music: Space Sound Effects",
            "",
            "Press SPACE to return to the main menu"
        ]

        self.start_pos = self.height
        self.current_pos = self.start_pos
        self.scroll_speed = 40.0
        self.started = False
        self.finished = False
        self.start_time = 0

        # Зоряне небо (зірки)
        self.stars = []
        self.generate_stars(200)

        # Звук
        try:
            self.intro_music = pygame.mixer.Sound('D:/Save/intro.mp3')
        except:
            print("Неможливо завантажити музику для кінцевих титрів. Переконайтеся, що файл існує.")
            self.intro_music = None

    def generate_stars(self, count):
        """Генерує зірки для фону"""
        import random
        for _ in range(count):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            size = random.randint(1, 3)
            brightness = random.randint(100, 255)
            self.stars.append((x, y, size, brightness))

    def start(self):
        self.started = True
        self.finished = False
        self.current_pos = self.start_pos
        self.start_time = pygame.time.get_ticks()

        # Відтворення музики, якщо вона доступна
        if self.intro_music:
            self.intro_music.play()

    def update(self, dt):
        if not self.started:
            return

        # Рухаємо текст вгору
        self.current_pos -= self.scroll_speed * dt

        # Перевіряємо, чи титри закінчилися
        total_text_height = len(self.credits) * self.text_font.get_height() + 200
        if self.current_pos < -total_text_height:
            self.finished = True
            self.started = False
            if self.intro_music:
                self.intro_music.stop()

    def draw(self):
        if not self.started:
            return

        # Заповнюємо екран чорним кольором
        self.screen.fill((0, 0, 0))

        # Малюємо зірки
        for x, y, size, brightness in self.stars:
            pygame.draw.circle(self.screen, (brightness, brightness, brightness), (x, y), size)

        # Малюємо заголовок (постійно вгорі)
        title_surface = self.title_font.render(self.title_text, True, self.yellow)
        title_rect = title_surface.get_rect(center=(self.width // 2, 100))
        self.screen.blit(title_surface, title_rect)

        # Малюємо текст, що рухається
        y_offset = self.current_pos

        for line in self.credits:
            if not line:  # Порожній рядок
                y_offset += self.text_font.get_height() // 2
                continue

            text_surface = self.text_font.render(line, True, self.yellow)
            text_rect = text_surface.get_rect(center=(self.width // 2, y_offset))

            # Застосовуємо перспективу
            perspective_factor = 1.0 - (y_offset - self.height // 2) / (self.height * 1.5)
            if 0.3 <= perspective_factor <= 1.0:
                scaled_width = int(text_surface.get_width() * perspective_factor)
                scaled_height = int(text_surface.get_height() * perspective_factor)
                if scaled_width > 0 and scaled_height > 0:
                    scaled_surface = pygame.transform.scale(text_surface, (scaled_width, scaled_height))
                    scaled_rect = scaled_surface.get_rect(center=(self.width // 2, y_offset))
                    self.screen.blit(scaled_surface, scaled_rect)

            y_offset += self.text_font.get_height() * 1.2

    def skip(self):
        if self.started:
            self.finished = True
            self.started = False
            if self.intro_music:
                self.intro_music.stop()
            return True
        return False

    def is_finished(self):
        return self.finished