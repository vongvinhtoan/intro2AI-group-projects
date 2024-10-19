import pygame
from .resource_holder import ResourceHolder

class TextureHolder(ResourceHolder):
    def __init__(self):
        super().__init__()
    def add(self, key, value):
        super().add(key, pygame.image.load(value))