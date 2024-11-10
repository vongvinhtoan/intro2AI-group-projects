import pygame
from .scene_node import SceneNode

class GameEngine:
    def __init__(self, size, title):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True

        self.root_node = SceneNode()

        self.is_paused = False

    def set_window_size(self, size):
        self.screen = pygame.display.set_mode(size)

    def add_node(self, node):
        self.root_node.add_child(node)

    def run(self):
        while self.running:
            self.handle_events()

            dt = self.clock.tick(60) / 1000.0
            if not self.is_paused:
                self.root_node.update_all(dt)

            self.render()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.is_paused = not self.is_paused
                elif event.key == pygame.K_ESCAPE:
                    self.running = False

    def render(self):
        self.screen.fill((0, 0, 0))
        self.root_node.render(self.screen)
        pygame.display.flip()