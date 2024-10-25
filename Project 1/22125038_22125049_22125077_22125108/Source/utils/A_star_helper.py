import numpy as np
from munkres import Munkres

def manhattan(a: np.ndarray, b: np.ndarray) -> int:
    return np.sum(np.abs(a - b))

def minimum_cost_perfect_matching(cost_matrix):
    return sum(cost_matrix[i][j] for i, j in Munkres().compute(cost_matrix))