from .Search_strategy import Search_strategy
from problem import *

class BFS_strategy(Search_strategy):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "BFS"

    def search(self, problem: Problem, result: SearchOutput) -> None:
        super().search(problem, result)
        
        result.commit(0, 0, 0, "uLulDrrRRRRRRurD")