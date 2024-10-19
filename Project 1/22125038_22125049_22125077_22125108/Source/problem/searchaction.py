import numpy as np

action_map : dict[str, np.ndarray] = {
    "u": np.array([-1, 0]),
    "d": np.array([1, 0]),
    "l": np.array([0, -1]),
    "r": np.array([0, 1]),
}

class Action:
    def __init__(self, action: str):
        self.action = action

    def __str__(self):
        return f"Action: {self.action}, Direction: {action_map[self.action.lower()]}"