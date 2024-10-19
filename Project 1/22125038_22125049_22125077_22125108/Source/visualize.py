import visualize.component.root as root
import visualize.component.ui as ui
from state import *
import numpy as np

game = root.GameEngine(800, 600, "Game Engine")

TRANSPARENT = -9999999

def refine_state(s):
    cell = [[cellType(c) for c in r] for r in s]
    background = [[c if c in (WALL, SWITCH) else EMPTY for c in r] for r in cell]
    foreground = [[AGENT if c in (AGENT, AGENT_SWITCH) else STONE if c in (STONE, STONE_SWITCH) else TRANSPARENT for c in r] for r in cell]
    w = [[weight(c) for c in r] for r in s]
    return [background, foreground], w

textureHolder = root.TextureHolder()
textureHolder.add(EMPTY, "visualize/resources/empty.png")
textureHolder.add(AGENT, "visualize/resources/agent.png")
textureHolder.add(STONE, "visualize/resources/stone.png")
textureHolder.add(WALL, "visualize/resources/wall.png")
textureHolder.add(SWITCH, "visualize/resources/switch.png")
textureHolder.add(TRANSPARENT, "visualize/resources/transparent.png")

fontHolder = root.FontHolder()
fontHolder.add("default", ("visualize/resources/Arial.ttf", 24))

red_square = ui.RectangleView((100, 100), (100, 100), (255, 0, 0))

currentState = SearchState("/home/nhphucqt/Documents/MyLabs/intro2AI-group-projects/Project 1/22125038_22125049_22125077_22125108/Source/input-01.txt")

boardView = ui.BoardView((0, 0), 64, currentState.state.shape[0], currentState.state.shape[1], textureHolder, fontHolder)

board, w = refine_state(currentState.state)
print(board)
boardView.set_board(board, w)

game.add_node(boardView)

game.run()