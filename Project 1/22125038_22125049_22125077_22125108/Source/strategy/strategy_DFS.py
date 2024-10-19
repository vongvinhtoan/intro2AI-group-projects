from .searchstrategy import SearchStrategy
from problem import *

class Strategy_DFS(SearchStrategy):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "DFS"

    def search(self, problem: Problem) -> SearchNode|None:
        super().search(problem)

        node = SearchNode(problem.initial_state)
        node = SearchNode(problem.initial_state)
        
        return node