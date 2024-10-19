import numpy as np
import itertools
from typing import TextIO
from .searchstate import SearchState

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

    @property
    def shape(self):
        return self.map_layer.shape

    def parse_input(self, input_stream: TextIO, initial_state: SearchState) -> None:
        lines = input_stream.readlines()
        self.stone_weights = np.array(list(map(int, lines[0].split())), dtype=np.int64)
        lines = lines[1:]

        self.map_layer = np.array([list(line[:-1]) for line in lines])
        for row, col in itertools.product(range(len(self.map_layer)), range(len(self.map_layer[0]))):
            if self.map_layer[row, col] in [AGENT, STONE]:
                if self.map_layer[row, col] == AGENT:
                    initial_state.agent_position = (row, col)
                if self.map_layer[row, col] == STONE:
                    initial_state.stone_positions.append((row, col))
                if self.map_layer[row, col] == SWITCH:
                    self.switch_positions.append((row, col))
                self.map_layer[row, col] = EMPTY
            elif self.map_layer[row, col] in [AGENT_SWITCH, STONE_SWITCH]:
                if self.map_layer[row, col] == AGENT_SWITCH:
                    initial_state.agent_position = (row, col)
                if self.map_layer[row, col] == STONE_SWITCH:
                    initial_state.stone_positions.append((row, col))
                self.map_layer[row, col] = SWITCH
            
            if self.map_layer[row, col] == SWITCH:
                self.switch_positions.append((row, col))

        initial_state.stone_positions = np.array(initial_state.stone_positions, dtype=np.int32)
        initial_state.agent_position  = np.array(initial_state.agent_position, dtype=np.int32)
        
    def __str__(self):
        return '\n'.join([''.join(row) for row in self.map_layer])
    def __getitem__(self, key):
        return self.map_layer[key]
    def __setitem__(self, key, value):
        self.map_layer[key] = value
