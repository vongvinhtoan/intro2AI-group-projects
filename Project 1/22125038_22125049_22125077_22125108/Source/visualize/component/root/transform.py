import pygame

class Transform:
    def __init__(self, position: pygame.Vector2 =  (0, 0)):
        self.position = pygame.Vector2(position)

    def combine(self, other) -> 'Transform':
        combined_position = other.position + self.position
        return Transform(combined_position)
    
    def transform_rect(self, rect: pygame.Rect) -> pygame.Rect:
        return pygame.Rect(rect.topleft + self.position, rect.size)
    
    def transform_point(self, point: pygame.Vector2) -> pygame.Vector2:
        return point + self.position
    
    def translate(self, offset) -> None:
        self.position += offset