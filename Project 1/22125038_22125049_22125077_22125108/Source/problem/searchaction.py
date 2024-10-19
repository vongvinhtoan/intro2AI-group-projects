action_map : dict[str, tuple[int, int]] = {
    "u": (-1, 0),
    "d": (1, 0),
    "l": (0, -1),
    "r": (0, 1)
}

class Action:
    def __init__(self, action: str):
        self.action = action

    def __str__(self):
        return f"Action: {self.action}, Direction: {action_map[self.action.lower()]}"