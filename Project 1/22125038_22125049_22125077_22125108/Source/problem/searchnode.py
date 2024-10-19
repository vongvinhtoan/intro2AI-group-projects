from .searchstate import SearchState
from .searchaction import Action

class SearchNode:
    node_count = 0

    @classmethod
    def clear(cls):
        cls.node_count = 0

    def __init__(self, state: SearchState, parent: 'SearchNode' = None, action: Action = None, path_cost: int = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        SearchNode.node_count += 1

    def copy(self) -> 'SearchNode':
        return SearchNode(self.state.copy(), self.parent, self.action, self.path_cost)
    
    def __eq__(self, other: 'SearchNode') -> bool:
        pass 

    def __hash__(self) -> int:
        pass