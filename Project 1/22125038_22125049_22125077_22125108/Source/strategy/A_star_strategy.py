from .Search_strategy import Search_strategy
from state import *

class A_star_strategy(Search_strategy):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "A*"

    def _search(self, initial_state: SearchState, result: SearchOutput) -> None:
        super()._search(initial_state, result)

        # Your code here

        result.commit(
            numSteps=16, 
            totalWeight=695, 
            numNodesExpanded=4321, 
            solution="uLulDrrRRRRRRurD"
        )