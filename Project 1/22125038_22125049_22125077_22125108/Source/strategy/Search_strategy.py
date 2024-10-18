from state import *
import tracemalloc
import time

class Search_strategy:
    def __init__(self):
        self.initial_state = None
        self.result = SearchOutput(str(self))

    def set_initial_state(self, initial_state: SearchState):
        self.initial_state = initial_state

    def _search(self, initial_state: SearchState, result: SearchOutput) -> None:
        print(f"{str(self)} search")

    def search(self) -> SearchOutput:
        tracemalloc.start()
        start_time = time.time()

        self.result = SearchOutput(str(self))
        self._search(self.initial_state, self.result)
        
        end_time = time.time()
        consumed_time = end_time - start_time
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        memory = peak / 10**6
        
        self.result.time = consumed_time
        self.result.memory = memory

        return self.result

    def __str__(self):
        return self.__class__.__name__