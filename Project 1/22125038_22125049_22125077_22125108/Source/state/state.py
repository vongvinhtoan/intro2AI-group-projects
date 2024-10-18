import numpy as np
import itertools

STONE = -1
EMPTY = 0
AGENT = 1
WALL = 2
SWITCH = 4
STONE_SWITCH = 8
AGENT_SWITCH = 6

agent_directions = {
    'u': (-1, 0),
    'd': (1, 0),
    'l': (0, -1),
    'r': (0, 1)
}

value_map = {
    '#': WALL,
    ' ': EMPTY,
    '$': STONE,
    '@': AGENT,
    '.': SWITCH,
    '*': STONE_SWITCH,
    '+': AGENT_SWITCH
}

char_map = {value: key for key, value in value_map.items()}
def cellType(cell):
    if cell < 0:
        return STONE
    if cell > max(value_map.values()):
        return STONE_SWITCH
    return cell

def weight(cell):
    if cell < 0:
        return -cell
    if cell > max(value_map.values()):
        return cell - max(value_map.values())
    return 0

def removeStone(cell):
    if cellType(cell) == STONE:
        return EMPTY
    if cellType(cell) == STONE_SWITCH:
        return SWITCH
    assert False, "Cannot remove stone from cell"

def addStone(cell, w):
    if cellType(cell) == EMPTY:
        return -w
    if cellType(cell) == SWITCH:
        return w + max(value_map.values())
    assert False, "Cannot add stone to cell"

def addAgent(cell):
    if cellType(cell) == EMPTY:
        return AGENT
    if cellType(cell) == SWITCH:
        return AGENT_SWITCH
    assert False, "Cannot add agent to cell"

def removeAgent(cell):
    if cellType(cell) == AGENT:
        return EMPTY
    if cellType(cell) == AGENT_SWITCH:
        return SWITCH
    assert False, "Cannot remove agent from cell"

class SearchState:
    def __init__(self, input_state: str|np.ndarray):
        self.state = None
        self.agentPosition = None
        if type(input_state) == np.ndarray:
            self.state = input_state.copy()
        else:
            self.parse_input(input_state)

        for row, col in itertools.product(range(len(self.state)), range(len(self.state[0]))):
            if cellType(self.state[row, col]) in [AGENT, AGENT_SWITCH]:
                self.agentPosition = (row, col)

    def parse_input(self, file_input: str):
        with open(file_input, 'r') as f:
            lines = f.readlines()
            weights = list(map(int, lines[0].split()))
            lines = lines[1:]

            def toCell(char):
                try:
                    if cellType(value_map[char]) == STONE:
                        return -weights.pop(0)
                    if cellType(value_map[char]) == STONE_SWITCH:
                        return weights.pop(0) + max(value_map.values())
                except IndexError:
                    raise ValueError("The input file does not contain enough weights")
                return value_map[char]
            
            self.state = np.array([list(map(toCell, line[:-1])) for line in lines])

    def __str__(self):
        weights = []
        for row, col in itertools.product(range(len(self.state)), range(len(self.state[0]))):
            cell = self.state[row, col]
            if cellType(cell) in [STONE, STONE_SWITCH]:
                weights.append(int(weight(cell)))
        
        string = ''
        string += str(weights) + '\n'
        string += '\n'.join([''.join([str(char_map[cellType(cell)]) for cell in row]) for row in self.state])
        return string