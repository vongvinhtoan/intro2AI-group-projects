import pygame
import numpy as np

from ..root.scene_node import SceneNode
from ..root.transform import Transform

from visualize.component.root import TextureHolder, FontHolder
from problem import Problem, SearchState
from problem.environment import *

class BoardView(SceneNode):
    def __init__(self, position: tuple[int], drawSize: tuple[int], problem: Problem, solution: str, textureHolder: TextureHolder, fontHolder: FontHolder):
        super().__init__()
        self.transform = Transform(position)

        self.numRow = problem.environment.shape[0]
        self.numCol = problem.environment.shape[1]
        
        self.problem = problem
        self.state = problem.initial_state
        self.boardName = solution["name"]
        self.solution = solution["move"].lower()

        self.statusRect = pygame.Rect(0, drawSize[1]-50, drawSize[0], 50)

        self.cellSize = min(drawSize[0] // self.numCol, (drawSize[1]-self.statusRect.size[1]) // self.numRow)
        self.cellRect = pygame.Rect(0, 0, self.cellSize, self.cellSize)

        self.sprite = {
            EMPTY: pygame.transform.scale(textureHolder.get(EMPTY), (self.cellSize, self.cellSize)),
            AGENT: pygame.transform.scale(textureHolder.get(AGENT), (self.cellSize, self.cellSize)),
            STONE: pygame.transform.scale(textureHolder.get(STONE), (self.cellSize, self.cellSize)),
            WALL: pygame.transform.scale(textureHolder.get(WALL), (self.cellSize, self.cellSize)),
            SWITCH: pygame.transform.scale(textureHolder.get(SWITCH), (self.cellSize, self.cellSize))
        }
        self.font = fontHolder.get("default")

        self.background = pygame.Surface((self.numCol * self.cellSize, self.numRow * self.cellSize))
        for y in range(self.numRow):
            for x in range(self.numCol):
                self.cellRect.topleft = (x * self.cellSize, y * self.cellSize)
                self.background.blit(self.sprite[self.problem.environment.map_layer[y,x]], self.cellRect.topleft)

        self.timeStep = 1
        self.timeCounter = 0
        self.currentStep = 0
        self.numSteps = len(self.solution)
        self.cost = 0

    def size(self) -> tuple[int]:
        return (self.numCol * self.cellSize, self.numRow * self.cellSize)

    def update(self, dt: float) -> None:
        self.timeCounter += dt
        if self.timeCounter > self.timeStep:
            self.timeCounter -= self.timeStep

            if self.currentStep < self.numSteps:
                actions = self.problem.actions(self.state)
                action = self.solution[self.currentStep]
                for a in actions:
                    if a.action == action:
                        self.state, cost = self.problem.result(self.state, a)
                        self.cost += cost
                        break
                self.currentStep += 1

    def __draw_rounded_rect(self, surface: pygame.Surface, color: tuple[int], rect: pygame.Rect, corner_radius: int) -> None:
        shape_surf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)  # Use SRCALPHA for transparency
        pygame.draw.rect(shape_surf, color, shape_surf.get_rect(), border_radius=corner_radius)
        surface.blit(shape_surf, rect.topleft)

    def draw(self, surface: pygame.Surface, global_transform: Transform) -> None:
        # Draw background
        surface.blit(self.background, global_transform.transform_point(pygame.Vector2(0, 0)))

        # Draw agent
        self.cellRect.center = (self.state.agent_position[1] * self.cellSize + self.cellSize/2, self.state.agent_position[0] * self.cellSize + self.cellSize/2)
        surface.blit(self.sprite[AGENT], global_transform.transform_rect(self.cellRect))

        # Draw stones
        for position, weight in zip(self.state.stone_positions, self.problem.environment.stone_weights):
            self.cellRect.center = (position[1] * self.cellSize + self.cellSize/2, position[0] * self.cellSize + self.cellSize/2)
            surface.blit(self.sprite[STONE], global_transform.transform_rect(self.cellRect))
            
            text = self.font.render(str(weight), True, (255, 255, 255))
            rect = text.get_rect()
            rect.center = (position[1] * self.cellSize + self.cellSize // 2, position[0] * self.cellSize + self.cellSize // 2)
            rect = global_transform.transform_rect(rect)
            round_rect = rect.inflate(10, 10)
            self.__draw_rounded_rect(surface, (0,0,0,128), round_rect, 20)
            surface.blit(text, rect)

        # Draw status bar
        textLeft = self.font.render(f"{self.boardName}", True, (255, 255, 255))
        textRight = self.font.render(f"Step: {self.currentStep}/{self.numSteps} - Cost: {self.cost}", True, (255, 255, 255))
        
        rect = textLeft.get_rect()
        rect.topleft = (10, 10)
        surface.blit(textLeft, global_transform.transform_rect(rect).move(0, self.statusRect.top))

        rect = textRight.get_rect()
        rect.topright = (self.size()[0]-10, 10)
        surface.blit(textRight, global_transform.transform_rect(rect).move(0, self.statusRect.top))