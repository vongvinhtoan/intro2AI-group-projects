from typing import Generator
from .searchstrategy import SearchStrategy
from problem import *

class Strategy_DFS(SearchStrategy):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "DFS"

    def search(self, problem: Problem) -> SearchNode|None:
        node = SearchNode(problem.initial_state)
        dfsStack: list[tuple[SearchNode, Generator[SearchNode, None, None]]] = [(node, problem.expand(node))]
        visited : set[SearchState] = {problem.initial_state}

        while len(dfsStack) > 0:
            node, expand = dfsStack[-1]
            try:
                child = next(expand)
                if problem.is_goal(child.state):
                    return child
                if child.state not in visited:
                    visited.add(child.state)
                    dfsStack.append((child, problem.expand(child)))
            except StopIteration:
                visited.remove(node.state)
                dfsStack.pop()
                
        return None
    