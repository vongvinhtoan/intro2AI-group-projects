from typing import Generator
from .environment import Environment
from .searchstate import SearchState

class Problem:
    class Action:
        def __init__(self, name, direction):
            self.name = name
            self.direction = direction

        def __str__(self):
            return f"Action: {self.name}, Direction: {self.direction}"

    def __init__(self):
        self.initialState = SearchState()
        self.environment = Environment()

    def parse_input(self, input_file: str):
        pass

    def is_goal(self, state: SearchState) -> bool:
        pass
    
    def actions(self, state: SearchState) -> Generator[Action, None, None]:
        pass

    def result(self, state: SearchState, action: Action) -> tuple[SearchState, int]:
        pass
    
    