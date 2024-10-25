from problem import *
import tracemalloc
import time
from .infospinner import InfoSpinner, SpinnerStopCode
from concurrent.futures import ThreadPoolExecutor
from problem.searchexception import SearchException

class SearchStrategy:
    def __init__(self):
        self._info_spinner = InfoSpinner()
        self._time_limit_exceeded = False
        self._memory_limit_exceeded = False
        self._user_interrupted = False
        self._start_time = 0

    def search(self, problem: Problem) -> SearchNode|None:
        pass

    def solve(self, problem: Problem, time_limit: float = -1, memory_limit: float = -1) -> ProblemResult:
        print("="*20 + f"\n{str(self)} search")

        self._monitor_reset()

        verdict = "No solution found"
        result = ProblemResult()
        result.strategy_name = str(self)
        search_result = None
        with ThreadPoolExecutor() as executor:
            try:
                search_result_future = executor.submit(self.search, problem)
                while not search_result_future.done():
                    self._monitor_check(time_limit, memory_limit)
                    if self._time_limit_exceeded or self._memory_limit_exceeded: SearchNode.block()
                    time.sleep(0.1)
                search_result = search_result_future.result()
                self._info_spinner.stop(SpinnerStopCode.FINISHED)
            except KeyboardInterrupt:
                self._user_interrupted = True
                SearchNode.block()
                self._info_spinner.stop(SpinnerStopCode.INTERRUPTED)
            except SearchException as e:
                if self._time_limit_exceeded:
                    self._info_spinner.stop(SpinnerStopCode.TLE)
                    verdict = "Time limit exceeded"
                elif self._memory_limit_exceeded:
                    self._info_spinner.stop(SpinnerStopCode.MLE)
                    verdict = "Memory limit exceeded"
                elif self._user_interrupted:
                    self._info_spinner.stop(SpinnerStopCode.INTERRUPTED)
                    verdict = "User interrupted"
            except Exception as e:
                self._info_spinner.stop(SpinnerStopCode.ERROR)
                print(e)
                raise e
        
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        result.set_result(search_result, problem, verdict)
        result.time = time.time() - self._start_time
        result.memory = peak / 10**6
        result.numNodeGenerated = SearchNode.node_count

        return result

    def _monitor_reset(self):
        self._memory_limit_exceeded = False
        self._time_limit_exceeded = False
        self._user_interrupted = False
        SearchNode.clear()
        self._start_time = time.time()
        self._info_spinner.start(self._start_time)
        tracemalloc.start()

    def _monitor_check(self, time_limit: float, memory_limit: int):
        _, peak = tracemalloc.get_traced_memory()
        if time.time() - self._start_time > time_limit and time_limit > 0:
            self._time_limit_exceeded = True
        if peak / 10**6 > memory_limit and memory_limit > 0:
            self._memory_limit_exceeded = True

    def __str__(self):
        return self.__class__.__name__