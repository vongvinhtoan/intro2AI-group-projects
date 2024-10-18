import numpy as np
import itertools

STONE = -1
EMPTY = 0
AGENT = 1
WALL = 2
SWITCH = 4
STONE_SWITCH = 8
AGENT_SWITCH = 6

value_map = {
    '#': WALL,
    ' ': EMPTY,
    '$': STONE,
    '@': AGENT,
    '.': SWITCH,
    '*': STONE_SWITCH,
    '+': AGENT_SWITCH
}

max_value = max(value_map.values())

char_map = {value: key for key, value in value_map.items()}
def cellType(cell):
    if cell < 0:
        return STONE
    if cell > max_value:
        return STONE_SWITCH
    return cell

def weight(cell):
    if cell < 0:
        return -cell
    if cell > max_value:
        return cell - max_value
    return 0

class SearchState:
    def __init__(self, file_input: str):
        self.state = None
        self.parse_input(file_input)

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
                        return weights.pop(0) + max_value
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