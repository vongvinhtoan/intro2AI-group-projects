from .searchstrategy import SearchStrategy
from problem import *
from collections import deque

class Strategy_DFS(SearchStrategy):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "DFS"
    
    def search(self, problem: Problem) -> SearchNode|None:
        frontier : deque[SearchNode] = deque([SearchNode(problem.initial_state)])
        visited : set[SearchState] = set()
        visited.add(problem.initial_state)

        while frontier:
            node = frontier.pop()
            assert node.state in visited
            visited.remove(node.state)
            if problem.is_goal(node.state):
                return node
            if node.state not in visited:
                for child in problem.expand(node):
                    frontier.append(child)
                    visited.add(child.state)
        return None
    