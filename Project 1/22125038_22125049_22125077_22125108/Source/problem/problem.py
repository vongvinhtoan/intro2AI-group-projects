from typing import Generator, TextIO
from .environment import *
from .searchstate import SearchState
from .searchnode import SearchNode
from .searchaction import Action, action_map

class Problem:
    def __init__(self):
        self.initial_state = SearchState()
        self.environment = Environment()

    def parse_input(self, input_stream: TextIO) -> None: 
        self.environment.parse_input(input_stream, self.initial_state)

    def is_goal(self, state: SearchState) -> bool:
        for position in state.stone_positions:
            if self.environment[position] != SWITCH:
                return False
        return True
    
    def actions(self, state: SearchState) -> Generator[Action, None, None]:
        def is_valid_position(position: tuple[int, int], direction: tuple[int, int]) -> bool:
            row, col = position
            drow, dcol = direction
            row += drow; col += dcol
            if row < 0 or row >= self.environment.shape[0] or col < 0 or col >= self.environment.shape[1]: return False
            if self.environment[row, col] == WALL: return False
            if (row, col) in state.stone_positions:
                if self.environment[row + drow, col + dcol] == WALL: return False
                if (row + drow, col + dcol) in state.stone_positions: return False
            return True
        
        for action, direction in action_map.items():
            if is_valid_position(state.agent_position, direction):
                yield Action(action)

    def result(self, state: SearchState, action: Action) -> tuple[SearchState, int]:
        drow, dcol = action_map[action.action]
        new_state = state.copy()
        new_state.agent_position = (new_state.agent_position[0] + drow, new_state.agent_position[1] + dcol)
        action_cost = 1
        for i, position in enumerate(new_state.stone_positions):
            if position == new_state.agent_position:
                new_state.stone_positions[i] = (position[0] + drow, position[1] + dcol)
                action_cost += self.environment.stone_weights[i]
                break
        return new_state, action_cost

    def expand(self, node: SearchNode) -> Generator[SearchNode, None, None]:
        state = node.state
        for action in self.actions(state):
            child, action_cost = self.result(state, action)
            yield SearchNode(child, node, action, node.path_cost + action_cost)
    
    def to_str(self, state: SearchState) -> str:
        map = self.environment.map_layer.copy()
        if map[state.agent_position[0], state.agent_position[1]] == SWITCH:
            map[state.agent_position[0], state.agent_position[1]] = AGENT_SWITCH
        else:
            map[state.agent_position[0], state.agent_position[1]] = AGENT
        stone_positions, stone_weights = state.stone_positions, self.environment.stone_weights
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
        return string