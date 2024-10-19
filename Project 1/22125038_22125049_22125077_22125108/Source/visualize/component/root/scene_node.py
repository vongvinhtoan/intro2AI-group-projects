import pygame
import math
from .transform import Transform

class SceneNode:
    def __init__(self):
        self.transform = Transform()
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def remove_child(self, child):
        child.parent = None
        self.children.remove(child)

    def draw(self, surface, parent_transform=Transform()):
        pass

    def update(self, dt):
        pass

    def render(self, surface, parent_transform=Transform()):
        # Combine this node's transform with the parent's transform
        combined_transform = self.transform.combine(parent_transform)

        # Draw the current node with the combined transform
        self.draw(surface, combined_transform)

        # Recursively render all children
        for child in self.children:
            child.render(surface, combined_transform)

    def update_all(self, dt):
        # Update the current node
        self.update(dt)

        # Recursively update all children
        for child in self.children:
            child.update_all(dt)