from . import strategy_A_star, strategy_BFS, strategy_DFS, strategy_UCS
from .searchstrategy import SearchStrategy

DFS_solver = strategy_DFS.Strategy_DFS()
BFS_solver = strategy_BFS.Strategy_BFS()
UCS_solver = strategy_UCS.Strategy_UCS()
A_star_solver = strategy_A_star.Strategy_A_star()

solver_dict : dict[str, SearchStrategy] = {
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