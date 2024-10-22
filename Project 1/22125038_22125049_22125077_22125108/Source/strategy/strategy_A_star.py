from .searchstrategy import SearchStrategy
from problem import *
from . import best_first_search

class Strategy_A_star(SearchStrategy):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "A*"

    def search(self, problem: Problem) -> SearchNode|None:
        return best_first_search.search(problem, lambda node: node.path_cost + problem.heuristic(node.state))