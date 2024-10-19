from .searchnode import SearchNode
from .problem import Problem

class ProblemResult:
    def __init__(self):
        self.strategy_name = ""
        self.numSteps = 0
        self.totalWeight = 0
        self.numNodeGenerated = 0
        self.time = 0
        self.memory = 0
        self.solution = ""

    def set_result(self, node: SearchNode, problem: Problem):
        if node is not None and problem.is_goal(node.state):
            self.totalWeight = node.path_cost
            self.solution = ""
            while node is not None:
                self.solution += f"{node.action}" if node.action is not None else ""
                node = node.parent
            self.numSteps = len(self.solution)
            self.solution = self.solution[::-1]
        else:
            if node is None:
                self.solution = "No solution found"
            elif not problem.is_goal(node.state):
                self.solution = "Returned node is not a goal state"
        self.numNodeGenerated = SearchNode.node_count

    def __str__(self):
        message = f"{self.strategy_name}"
        message += f"\nSteps: {self.numSteps}, Weight: {self.totalWeight}, Node: {self.numNodeGenerated}"
        message += f", Time (ms): {self.time:.2f}, Memory (MB): {self.memory:.2f}"
        message += f"\n{self.solution}"
        return message