from .searchstate import SearchState
from .searchaction import Action
import threading
from .searchexception import SearchException

class SearchNode:
    node_count = 0
    allow_creation = threading.Event()

    @classmethod
    def clear(cls):
        cls.node_count = 0
        cls.allow_creation.set()

    @classmethod
    def block(cls):
        cls.allow_creation.clear()

    def __init__(self, state: SearchState, parent: 'SearchNode' = None, action: Action = None, path_cost: int = 0):
        if not SearchNode.allow_creation.is_set():
            raise SearchException("SearchNode creation is not blocked")
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        SearchNode.node_count += 1

    def copy(self) -> 'SearchNode':
        return SearchNode(self.state.copy(), self.parent, self.action, self.path_cost)
    
    def __lt__(self, other: 'SearchNode') -> bool:
        return self.path_cost < other.path_cost