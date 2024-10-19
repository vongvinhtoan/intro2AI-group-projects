from .searchstrategy import SearchStrategy
from problem import *

class Strategy_A_star(SearchStrategy):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "A*"

    def search(self, problem: Problem) -> SearchNode|None:
        super().search(problem)

        node = SearchNode(problem.initial_state)
        node = SearchNode(problem.initial_state)

        print(problem.to_str(node.state))

        return node