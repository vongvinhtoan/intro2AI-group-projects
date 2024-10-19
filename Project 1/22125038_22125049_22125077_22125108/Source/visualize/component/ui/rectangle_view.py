import pygame
from ..root.scene_node import SceneNode
from ..root.transform import Transform

class RectangleView(SceneNode):
    def __init__(self, position, size, color):
        super().__init__()
        self.transform = Transform(position)
        self.size = size
        self.color = color

    def draw(self, surface, global_transform):
        # Use the global transform's position for drawing
        # Draw the rectangle at the calculated global position
        rect = pygame.Rect(global_transform.position, self.size)
        pygame.draw.rect(surface, self.color, global_transform.transform_rect(rect))