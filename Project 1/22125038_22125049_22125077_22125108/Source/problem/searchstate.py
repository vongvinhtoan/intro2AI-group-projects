import numpy as np

class SearchState:
    def __init__(self, agent_position: np.ndarray = np.array([-1, -1], dtype=np.int32), stone_positions: list[np.ndarray] = []):
        self.agent_position = agent_position
        self.stone_positions = stone_positions

    def copy(self):
        state = SearchState()
        state.agent_position = self.agent_position.copy()
        state.stone_positions = self.stone_positions.copy()
        return state