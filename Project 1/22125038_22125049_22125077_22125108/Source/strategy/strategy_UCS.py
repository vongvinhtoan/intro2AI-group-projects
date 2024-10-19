from .searchstrategy import SearchStrategy
from problem import *

from queue import PriorityQueue

class Strategy_UCS(SearchStrategy):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "UCS"

    def search(self, problem: Problem) -> SearchNode|None:
        super().search(problem)

        node = SearchNode(problem.initial_state)
        frontier : PriorityQueue[SearchNode] = PriorityQueue()

        frontier.put(node)
        reached = {node.state: node}

        while frontier:
            node = frontier.get()
            
            if problem.is_goal(node.state):
                return node
            
            if reached[node.state].path_cost < node.path_cost:
                continue

            for child in problem.expand(node):
                s = child.state
                if s not in reached or child.path_cost < reached[s].path_cost:
                    reached[s] = child
                    frontier.put(child)
        return None