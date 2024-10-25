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
            if self.environment[position[0], position[1]] != SWITCH:
                return False
        return True
    
    def is_valid_position(self, state: SearchState, direction: np.ndarray) -> bool:
        position = state.agent_position.copy()
        position += direction
        if not (0 <= position[0] < self.environment.shape[0] and 0 <= position[1] < self.environment.shape[1]): return False, None
        if self.environment[tuple(position)] == WALL: return False, None
        if np.any(np.all(state.stone_positions == position, axis=1)):
            if self.environment[tuple(position + direction)] == WALL: return False, None
            if np.any(np.all(state.stone_positions == position+direction, axis=1)): return False, None
            return True, True
        return True, False
    
    def actions(self, state: SearchState) -> Generator[Action, None, None]:
        for action, direction in action_map.items():
            valid, to_push = self.is_valid_position(state, direction)
            if valid:
                yield Action(action, to_push)

    def result(self, state: SearchState, action: Action) -> tuple[SearchState, int]:
        drow, dcol = action_map[action.action]
        new_state = state.copy()
        new_state.agent_position += np.array([drow, dcol], dtype=np.int32)
        action_cost = 1
        for i, position in enumerate(new_state.stone_positions):
            if np.array_equal(new_state.agent_position, position):
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

        map[tuple(state.agent_position)] = AGENT if map[tuple(state.agent_position)] != SWITCH else AGENT_SWITCH
        
        stone_positions, stone_weights = state.stone_positions, self.environment.stone_weights
        display_weights = []
        for position, weight in sorted(zip(stone_positions, stone_weights), key=lambda x: tuple(x[0])):
            map[tuple(position)] = STONE if map[tuple(position)] != SWITCH else STONE_SWITCH
            display_weights.append(int(weight))
        
        string = ''
        string += str(display_weights) + '\n'
        string += '\n'.join([''.join(row) for row in map])
        return string