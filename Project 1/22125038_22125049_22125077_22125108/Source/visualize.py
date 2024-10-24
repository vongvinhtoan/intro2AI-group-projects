import visualize.component.root as root
import visualize.component.ui as ui
import argparse
import json
from problem import Problem
from problem.environment import *

def prepare_resources():
    textureHolder = root.TextureHolder()
    textureHolder.add(EMPTY, "visualize/resources/empty.png")
    textureHolder.add(AGENT, "visualize/resources/agent.png")
    textureHolder.add(STONE, "visualize/resources/stone.png")
    textureHolder.add(WALL, "visualize/resources/wall.png")
    textureHolder.add(SWITCH, "visualize/resources/switch.png")

    fontHolder = root.FontHolder()
    fontHolder.add("default", ("visualize/resources/Arial.ttf", 24))

    return textureHolder, fontHolder

def main(args):
    maxWindowSize = (1600, 900)

    game = root.GameEngine(maxWindowSize, "Game Engine")

    textureHolder, fontHolder = prepare_resources()

    problem = Problem()
    problem.parse_input(open(args.map, 'r'))

    with open(args.sol, 'r') as f:
        solutions = json.load(f)

    assert len(solutions) <= 4, "Too many solutions"

    boardView = [ui.BoardView((0, 0), (maxWindowSize[0]//2,maxWindowSize[1]//2), problem, sol, textureHolder, fontHolder) for sol in solutions]
    padding = (50, 0)

    # 2x2 grid
    for i, bv in enumerate(boardView):
        # bv.transform.position = (i % 2 * bv.size()[0], i // 2 * bv.size()[1])
        bv.transform.position = (i % 2 * (bv.size()[0] + padding[0]), i // 2 * (bv.size()[1] + padding[1]))

    game.set_window_size((boardView[0].size()[0] * 2 + padding[0], boardView[0].size()[1] * 2 + padding[1]))

    for bv in boardView:
        game.add_node(bv)
    game.run()

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--map", type=str, help="Input file")
    args.add_argument("--sol", type=str, help="Solution file")

    args = args.parse_args()

    main(args)