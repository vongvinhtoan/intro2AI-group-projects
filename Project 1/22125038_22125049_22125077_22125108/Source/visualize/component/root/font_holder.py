import pygame
from .resource_holder import ResourceHolder

class FontHolder(ResourceHolder):
    def __init__(self):
        super().__init__()
    def add(self, key, value):
        super().add(key, pygame.font.Font(value[0], value[1]))