from .searchstrategy import SearchStrategy
from problem import *
from queue import PriorityQueue

class Strategy_A_star(SearchStrategy):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "A*"

    def search(self, problem: Problem) -> SearchNode|None:
        super().search(problem)

        node = SearchNode(problem.initial_state)
        
        for child in problem.expand(node):
            print(problem.to_str(child.state))

        return node