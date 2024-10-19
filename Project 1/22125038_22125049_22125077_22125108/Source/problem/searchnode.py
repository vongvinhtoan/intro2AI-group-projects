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
        self.node_id = SearchNode.node_count
        SearchNode.node_count += 1

    def copy(self):
        return SearchNode(self.state.copy(), self.parent, self.action, self.path_cost)