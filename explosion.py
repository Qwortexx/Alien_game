import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center_position, screen, is_boss=False):
        super().__init__()
        self.screen = screen
        self.is_boss = is_boss
        

        # Перевірка на правильність значень координат
        if not isinstance(center_position, tuple) or len(center_position) != 2:
            raise ValueError(f"Invalid center_position: {center_position}. It must be a tuple of (x, y).")

        x, y = center_position
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError(f"Coordinates must be numbers. Got: x={x}, y={y}")


        # Load and scale explosion image
        try:
            self.image = pygame.image.load("C:/Python/alien_game/burst.png").convert_alpha()
            EXPLOSION_SIZE = (200, 200) if self.is_boss else (50, 50)
            self.image = pygame.transform.scale(self.image, EXPLOSION_SIZE)
            print("Explosion image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading explosion image: {e}")
            # Create a fallback if image fails to load
            EXPLOSION_SIZE = (200, 200) if self.is_boss else (50, 50)
            self.image = pygame.Surface(EXPLOSION_SIZE)
            self.image.fill((255, 0, 0))  # Red square as fallback

        
        # Set position
        self.rect = self.image.get_rect(center=center_position)
        
        # Set how long the explosion stays on screen
        self.frame_count = 0
        self.max_frames = 15  # The explosion will stay for 15 frames
    
    def update(self):
        # Increment frame counter and kill the sprite if it's been displayed long enough
        self.frame_count += 1
        if self.frame_count >= self.max_frames:
            self.kill()
    
    def draw(self):
        self.screen.blit(self.image, self.rect)
