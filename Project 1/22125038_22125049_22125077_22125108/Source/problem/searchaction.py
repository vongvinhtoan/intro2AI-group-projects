import numpy as np

action_map : dict[str, np.ndarray] = {
    "u": np.array([-1, 0]),
    "d": np.array([1, 0]),
    "l": np.array([0, -1]),
    "r": np.array([0, 1]),
}

class Action:
    def __init__(self, action: str, to_push: bool):
        self.action = action
        self.to_push = to_push

    def __str__(self):
        return self.action if not self.to_push else self.action.upper()