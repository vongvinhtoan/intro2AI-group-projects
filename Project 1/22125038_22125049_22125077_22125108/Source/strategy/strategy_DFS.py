from .searchstrategy import SearchStrategy
from problem import *

class DSFState:
    def __init__(self, problem: Problem, node: SearchNode):
        self.node = node
        self.expand = problem.expand(node)

class Strategy_DFS(SearchStrategy):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "DFS"

    def search(self, problem: Problem) -> SearchNode|None:
        dfsStack: list[DSFState] = [DSFState(problem, SearchNode(problem.initial_state))]
        visited : set[SearchState] = {problem.initial_state}

        while len(dfsStack) > 0:
            dfsState = dfsStack[-1]
            print(problem.to_str(dfsState.node.state))
            try:
                child = next(dfsState.expand)
                if problem.is_goal(child.state):
                    return child
                if child.state not in visited:
                    visited.add(child.state)
                    dfsStack.append(DSFState(problem, child))
            except StopIteration:
                # visited.remove(dfsState.node.state)
                dfsStack.pop()
                
        return None
    