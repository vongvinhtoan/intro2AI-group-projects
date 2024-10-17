from .Search_strategy import Search_strategy
from state import *

class BFS_strategy(Search_strategy):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "BFS"

    def _search(self) -> SearchOutput:
        super()._search()
        state = self.state
        return SearchOutput(str(self))