import numpy as np

class SearchState:
    def __init__(self):
        self.agent_position = np.array([-1, -1], dtype=np.int32)
        self.stone_positions = []
        self.stone_weights = []

    def copy(self):
        state = SearchState()
        state.agent_position = self.agent_position.copy()
        state.stone_positions = self.stone_positions.copy()
        state.stone_weights = self.stone_weights.copy()
        return state