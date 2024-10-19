from problem import *

import tracemalloc
import time

class SearchStrategy:
    def __init__(self):
        self.state = None

    def set_state(self, state: SearchState):
        self.state = state

    def search(self, problem: Problem, result: SearchOutput) -> None:
        print(f"{str(self)} search")

    def solve(self, problem: Problem) -> SearchOutput:
        tracemalloc.start()
        start_time = time.time()
        result = SearchOutput(str(self))
        SearchNode.clear()

        self.search(problem, result)
        
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        result.time = time.time() - start_time
        result.memory = peak / 10**6
        result.numNodeGenerated = SearchNode.node_count

        return result

    def __str__(self):
        return self.__class__.__name__