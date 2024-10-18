import numpy as np
import itertools

STONE = '$'
EMPTY = ' '
AGENT = '@'
WALL = '#'
SWITCH = '.'
STONE_SWITCH = '*'
AGENT_SWITCH = '+'

agent_directions = {
    'u': (-1, 0),
    'd': (1, 0),
    'l': (0, -1),
    'r': (0, 1)
}

class Map:
    def __init__(self):
        self.map_layer = None
        self.switch_positions = []

    def parse_input(self, file_input: str):
        with open(file_input, 'r') as f:
            stone_positions = []
            stone_weights = None
            agent_position = None

            lines = f.readlines()
            stone_weights = np.array(list(map(int, lines[0].split())), dtype=np.int64)
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
            return agent_position, stone_positions, stone_weights
        
    def __str__(self):
        return '\n'.join([''.join(row) for row in self.map_layer])
    def __getitem__(self, key):
        return self.map_layer[key]
    def __setitem__(self, key, value):
        self.map_layer[key] = value

class SearchState:
    def __init__(self):
        self.map = Map()
        self.agent_position = None
        self.stone_positions = []
        self.stone_weights = []

    def parse_input(self, file_input: str):
        self.agent_position, self.stone_positions, self.stone_weights = self.map.parse_input(file_input)

    def __str__(self):
        map = self.map.map_layer.copy()
        if map[self.agent_position[0], self.agent_position[1]] == SWITCH:
            map[self.agent_position[0], self.agent_position[1]] = AGENT_SWITCH
        else:
            map[self.agent_position[0], self.agent_position[1]] = AGENT
        stone_positions, stone_weights = self.stone_positions, self.stone_weights
        tangled_stones = zip(stone_positions, stone_weights)
        tangled_stones = sorted(tangled_stones, key=lambda x: (x[0][0], x[0][1]))
        display_weights = []
        for position, weight in tangled_stones:
            if map[position[0], position[1]] == SWITCH:
                map[position[0], position[1]] = STONE_SWITCH
            else:
                map[position[0], position[1]] = STONE
            display_weights.append(int(weight))
        
        string = ''
        string += str(display_weights) + '\n'
        string += '\n'.join([''.join(row) for row in map])
        return str(string)
    
    def copy(self):
        state = SearchState()
        state.map = self.map
        state.agent_position = self.agent_position.copy()
        state.stone_positions = self.stone_positions.copy()
        state.stone_weights = self.stone_weights.copy()
        return state