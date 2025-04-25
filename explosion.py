import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center_position, screen):
        super().__init__()
        self.screen = screen
        
        # Load and scale explosion image
        try:
            self.image = pygame.image.load("C:/Python/alien_game/burst.png").convert_alpha()
            print("Explosion image loaded successfully!")
        except pygame.error as e:
            print(f"Error loading explosion image: {e}")
            # Create a fallback if image fails to load
            self.image = pygame.Surface((50, 50))
            self.image.fill((255, 0, 0))  # Red square as fallback
        
        # Scale the image
        self.image = pygame.transform.scale(self.image, (50, 50))
        
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
