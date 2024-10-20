from problem import *
import tracemalloc
import time
from .infospinner import InfoSpinner

class SearchStrategy:
    def __init__(self):
        self.state = None

    def set_state(self, state: SearchState):
        self.state = state

    def search(self, problem: Problem) -> SearchNode|None:
        pass

    def solve(self, problem: Problem) -> ProblemResult:
        print("="*20 + f"\n{str(self)} search")
        info_spinner = InfoSpinner()
        info_spinner.start()
        tracemalloc.start()
        start_time = time.time()

        result = ProblemResult()
        result.strategy_name = str(self)
        SearchNode.clear()

        try:
            result.set_result(self.search(problem), problem)
            info_spinner.stop()
        except KeyboardInterrupt:
            info_spinner.stop()
            print("\033[91mSearch interrupted by user.\033[0m")
        
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        result.time = time.time() - start_time
        result.memory = peak / 10**6
        result.numNodeGenerated = SearchNode.node_count

        return result

    def __str__(self):
        return self.__class__.__name__