import numpy as np

class SearchState:
    def __init__(self, agent_position: np.ndarray = np.array([-1, -1], dtype=np.int32), stone_positions: np.ndarray = np.array([[]], dtype=np.int32)):
        self.agent_position = agent_position
        self.stone_positions = stone_positions

    def copy(self):
        return SearchState(self.agent_position.copy(), self.stone_positions.copy())
    
    def __eq__(self, other: 'SearchState') -> bool:
        return np.array_equal(self.agent_position, other.agent_position) and np.array_equal(self.stone_positions, other.stone_positions)
    
    def __hash__(self) -> int:
        return hash((tuple(self.agent_position), tuple(self.stone_positions)))
    
    def __str__(self) -> str:
        return f"Agent: {self.agent_position}, Stones: {self.stone_positions}"