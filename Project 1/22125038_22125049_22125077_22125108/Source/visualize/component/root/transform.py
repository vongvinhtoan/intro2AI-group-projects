import pygame

class Transform:
    def __init__(self, position=(0, 0)):
        self.position = pygame.Vector2(position)

    def combine(self, other):
        combined_position = other.position + self.position
        return Transform(combined_position)
    
    def transform_rect(self, rect):
        return pygame.Rect(rect.topleft + self.position, rect.size)
    
    def translate(self, offset):
        self.position += offset