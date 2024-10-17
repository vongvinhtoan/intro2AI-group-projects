from . import A_star_strategy, BFS_strategy, DFS_strategy, UCS_strategy

DFS_solver = DFS_strategy.DFS_strategy()
BFS_solver = BFS_strategy.BFS_strategy()
UCS_solver = UCS_strategy.UCS_strategy()
A_star_solver = A_star_strategy.A_star_strategy()

solver_dict = {
    'DFS': DFS_solver,
    'BFS': BFS_solver,
    'UCS': UCS_solver,
    'A*': A_star_solver
}

__all__ = [
    'DFS_solver',
    'BFS_solver',
    'UCS_solver',
    'A_star_solver',
    'solver_dict',
]