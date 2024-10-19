from .searchstrategy import SearchStrategy
from problem import *

class Strategy_A_star(SearchStrategy):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "A*"

    def search(self, problem: Problem, result: SearchOutput) -> None:
        super().search(problem, result)

        node = SearchNode(problem.initial_state)
        node = SearchNode(problem.initial_state)
        node = SearchNode(problem.initial_state)
        node = SearchNode(problem.initial_state)

        print(problem.to_str(problem.initial_state))
        
        result.commit("uLulDrrRRRRRRurD", 0)