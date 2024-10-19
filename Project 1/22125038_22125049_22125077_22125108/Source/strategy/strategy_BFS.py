from .searchstrategy import SearchStrategy
from problem import *

class Strategy_BFS(SearchStrategy):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "BFS"

    def search(self, problem: Problem, result: SearchOutput) -> None:
        super().search(problem, result)
        
        node = SearchNode(problem.initial_state)
        node = SearchNode(problem.initial_state)
        
        result.commit("uLulDrrRRRRRRurD", 0)