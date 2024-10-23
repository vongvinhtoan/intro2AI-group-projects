from .searchstrategy import SearchStrategy
from problem import *
from collections import deque

class Strategy_DFS(SearchStrategy):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "DFS"

    def is_cycle(node: SearchNode) -> bool:
        current = node
        states = set()
        while current:
            if current.state in states:
                return True
            states.add(current.state)
            current = current.parent
        return False
    
    def search(self, problem: Problem) -> SearchNode|None:
        frontier = deque([SearchNode(problem.initial_state)])
        result = "failure"

        while frontier:
            node = frontier.pop()
            if problem.is_goal(node.state):
                return node
            if node.depth > limit:
                result = "cutoff"
            elif not self.is_cycle(node):
                for child in problem.expand(node):
                    frontier.append(child)
        return result