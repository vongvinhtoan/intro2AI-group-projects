from .searchstrategy import SearchStrategy
from problem import *

import heapq

class Strategy_UCS(SearchStrategy):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "UCS"

    def search(self, problem: Problem) -> SearchNode|None:
        super().search(problem)

        node = SearchNode(problem.initial_state)
        frontier : list[SearchNode] = []

        heapq.heappush(frontier, node)
        reached = {node.state: node}

        while frontier:
            node = heapq.heappop(frontier)
            # print(node.state, list(map(lambda x: x.state.__str__(), problem.expand(node))))

            if problem.is_goal(node.state):
                return node

            for child in problem.expand(node):
                s = child.state
                if s not in reached or child.path_cost < reached[s].path_cost:
                    reached[s] = child
                    heapq.heappush(frontier, child)
        return None