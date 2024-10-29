from .searchstrategy import SearchStrategy
from problem import *
from . import best_first_search
import numpy as np
from utils.A_star_helper import manhattan, minimum_cost_perfect_matching

class Strategy_A_star(SearchStrategy):
    def __init__(self):
        super().__init__()
        self.distances = []

    def __str__(self):
        return "A*"

    def distant_matrix(self, switch_position: np.ndarray, problem: Problem) -> int:
        def is_valid_position(position: np.ndarray) -> bool:
            return 0 <= position[0] < problem.environment.shape[0] and 0 <= position[1] < problem.environment.shape[1] and problem.environment[tuple(position)] != WALL
        distant = np.full(problem.environment.shape, np.inf)
        distant[tuple(switch_position)] = 0
        queue = [switch_position]
        while len(queue) > 0:
            current = queue.pop(0)
            for direction in action_map.values():
                next = current + direction
                if is_valid_position(next) and distant[tuple(next)] == np.inf:
                    distant[tuple(next)] = distant[tuple(current)] + 1
                    queue.append(next)
        return distant
    
    def initialize(self, problem: Problem) -> None:
        self.distances = [self.distant_matrix(switch_position, problem) for switch_position in problem.environment.switch_positions]
    
    def search(self, problem: Problem) -> SearchNode|None:
        self.initialize(problem)

        def heuristic1(state: SearchState) -> int:
            if problem.is_deadend(state):
                return np.inf
            cost_matrix = [[
                    manhattan(stone_position, goal_position) * (problem.environment.stone_weights[i] + 1)
                    for goal_position in problem.environment.switch_positions
                ] for i, stone_position in enumerate(state.stone_positions)
            ]
            return minimum_cost_perfect_matching(cost_matrix)
        
        def heuristic2(state: SearchState) -> int:
            if problem.is_deadend(state):
                return float('inf')
            cost_matrix = [[
                    distance[tuple(stone_position)] * (problem.environment.stone_weights[i] + 1) 
                    for distance in self.distances
                ] for i, stone_position in enumerate(state.stone_positions)
            ]
            return minimum_cost_perfect_matching(cost_matrix)

        # Run A* search with custom heuristic
        return best_first_search.search(problem, lambda node: node.path_cost + heuristic2(node.state))