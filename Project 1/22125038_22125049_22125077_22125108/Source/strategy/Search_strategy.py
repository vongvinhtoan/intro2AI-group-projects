from state import *
import tracemalloc
import time

class Search_strategy:
    def __init__(self):
        self.state = None

    def set_state(self, state: SearchState):
        self.state = state

    def _search(self) -> SearchOutput:
        print(f"{str(self)} search")

    def search(self) -> SearchOutput:
        tracemalloc.start()
        start_time = time.time()
        result = self._search()
        end_time = time.time()
        consumed_time = end_time - start_time
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        memory = peak / 10**6
        
        result.time = consumed_time
        result.memory = memory

        return result

    def __str__(self):
        return self.__class__.__name__