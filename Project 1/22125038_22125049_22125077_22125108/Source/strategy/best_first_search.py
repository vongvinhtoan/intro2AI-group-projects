from problem import *
from utils import PriorityQueue
from typing import Callable

def search(problem: Problem, f: Callable[[SearchNode], int]) -> SearchNode|None:
    node = SearchNode(problem.initial_state)
    
    frontier : PriorityQueue[SearchNode] = PriorityQueue(priority=f); frontier.put(node)
    reached : dict[SearchState, SearchNode] = {node.state: node}

    while not frontier.empty():
        node = frontier.get()
        
        if problem.is_goal(node.state):
            return node
        
        if f(reached[node.state]) < f(node):
            continue

        for child in problem.expand(node):
            s = child.state
            if s not in reached.keys() or f(child) < f(reached[s]):
                reached[s] = child
                frontier.put(child)
    return None