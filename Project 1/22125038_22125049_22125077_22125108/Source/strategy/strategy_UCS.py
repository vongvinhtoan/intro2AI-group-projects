from .searchstrategy import SearchStrategy
from problem import *

class Strategy_UCS(SearchStrategy):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "UCS"

    def search(self, problem: Problem, result: SearchOutput) -> None:
        super().search(problem, result)
        
        result.commit("uLulDrrRRRRRRurD", 0)