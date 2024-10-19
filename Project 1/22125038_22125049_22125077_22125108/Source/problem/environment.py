import numpy as np
import itertools

STONE = '$'
EMPTY = ' '
AGENT = '@'
WALL = '#'
SWITCH = '.'
STONE_SWITCH = '*'
AGENT_SWITCH = '+'

class Environment:
    def __init__(self):
        self.map_layer = None
        self.switch_positions = []
        self.stone_weights = []

    def parse_input_file(self, file_input: str):
        with open(file_input, 'r') as f:
            stone_positions = []
            agent_position = None

            lines = f.readlines()
            self.stone_weights = np.array(list(map(int, lines[0].split())), dtype=np.int64)
            lines = lines[1:]

            self.map_layer = np.array([list(line[:-1]) for line in lines])
            for row, col in itertools.product(range(len(self.map_layer)), range(len(self.map_layer[0]))):
                if self.map_layer[row, col] in [AGENT, STONE]:
                    if self.map_layer[row, col] == AGENT:
                        agent_position = (row, col)
                    if self.map_layer[row, col] == STONE:
                        stone_positions.append((row, col))
                    if self.map_layer[row, col] == SWITCH:
                        self.switch_positions.append((row, col))
                    self.map_layer[row, col] = EMPTY
                elif self.map_layer[row, col] in [AGENT_SWITCH, STONE_SWITCH]:
                    if self.map_layer[row, col] == AGENT_SWITCH:
                        agent_position = (row, col)
                    if self.map_layer[row, col] == STONE_SWITCH:
                        stone_positions.append((row, col))
                    self.map_layer[row, col] = SWITCH
                
                if self.map_layer[row, col] == SWITCH:
                    self.switch_positions.append((row, col))

            stone_positions = np.array(stone_positions, dtype=np.int32)
            agent_position = np.array(agent_position, dtype=np.int32)
            return agent_position, stone_positions
        
    def __str__(self):
        return '\n'.join([''.join(row) for row in self.map_layer])
    def __getitem__(self, key):
        return self.map_layer[key]
    def __setitem__(self, key, value):
        self.map_layer[key] = value