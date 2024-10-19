import pygame
import sys

from ..root.scene_node import SceneNode
from ..root.transform import Transform

class BoardView(SceneNode):
    def __init__(self, position, cellSize, numRow, numCol, textureHolder, fontHolder):
        super().__init__()
        self.transform = Transform(position)
        self.numRow = numRow
        self.numCol = numCol
        self.cellSize = cellSize
        self.textureHolder = textureHolder
        self.fontHolder = fontHolder

        print("BoardView: ", self.numRow, self.numCol)
        self.board = [[0 for x in range(self.numCol)] for y in range(self.numRow)]
        self.weight = [[0 for x in range(self.numCol)] for y in range(self.numRow)]

    def set_board(self, board, weight):
        self.board = board
        self.weight = weight

    def draw(self, surface, global_transform):
        for layer in self.board:
            for y in range(self.numRow):
                for x in range(self.numCol):
                    cell = layer[y][x]
                    image = pygame.transform.scale(self.textureHolder.get(cell), (self.cellSize, self.cellSize))
                    rect = pygame.Rect(x * self.cellSize, y * self.cellSize, self.cellSize, self.cellSize)
                    surface.blit(image, global_transform.transform_rect(rect))

        def draw_rounded_rect(surface, color, rect, corner_radius):
            shape_surf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)  # Use SRCALPHA for transparency
            pygame.draw.rect(shape_surf, color, shape_surf.get_rect(), border_radius=corner_radius)
            surface.blit(shape_surf, rect.topleft)

        for y in range(self.numRow):
            for x in range(self.numCol):
                if self.weight[y][x] != 0:
                    text = self.fontHolder.get("default").render(str(self.weight[y][x]), True, (255, 255, 255))
                    rect = text.get_rect()
                    rect.center = (x * self.cellSize + self.cellSize/2, y * self.cellSize + self.cellSize/2)
                    round_rect = rect.inflate(10, 10)
                    # pygame.draw.rect(surface, (255,255,255,200), rect.inflate(10, 10), border_radius=20)
                    draw_rounded_rect(surface, (0,0,0,128), round_rect, 20)
                    surface.blit(text, global_transform.transform_rect(rect))