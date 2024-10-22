from .searchstrategy import SearchStrategy
from problem import *
from queue import Queue

class Strategy_BFS(SearchStrategy):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "BFS"

    def search(self, problem: Problem) -> SearchNode|None:
        node = SearchNode(problem.initial_state)
        
        frontier : Queue[SearchNode] = Queue()
        frontier.put(node)
        reached = {node.state: node}
        
        while not frontier.empty():
            node = frontier.get()
            
            if problem.is_goal(node.state):
                return node
            
            for child in problem.expand(node):
                s = child.state
                if s not in reached:
                    reached[s] = child
                    frontier.put(child)

        return None