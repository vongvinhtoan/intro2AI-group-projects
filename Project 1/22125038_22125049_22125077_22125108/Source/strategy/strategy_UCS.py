from .searchstrategy import SearchStrategy
from problem import *

class Strategy_UCS(SearchStrategy):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "UCS"

    def search(self, problem: Problem) -> SearchNode|None:
        super().search(problem)

        node = SearchNode(problem.initial_state)

        return node