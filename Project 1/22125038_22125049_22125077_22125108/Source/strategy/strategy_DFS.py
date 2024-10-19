from .searchstrategy import SearchStrategy
from problem import *

class Strategy_DFS(SearchStrategy):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "DFS"

    def search(self, problem: Problem, result: SearchOutput) -> None:
        super().search(problem, result)
        
        result.commit("uLulDrrRRRRRRurD", 0)