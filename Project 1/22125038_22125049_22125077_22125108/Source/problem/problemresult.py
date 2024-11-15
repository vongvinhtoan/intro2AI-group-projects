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
        self.has_solution = False

    def set_result(self, node: SearchNode, problem: Problem, verdict: str = "No solution found"):
        if node is not None and problem.is_goal(node.state):
            self.totalWeight = node.path_cost
            self.solution = ""
            self.has_solution = True
            while node is not None:
                self.solution += f"{node.action}" if node.action is not None else ""
                node = node.parent
            self.numSteps = len(self.solution)
            self.solution = self.solution[::-1]
        else:
            if node is None:
                self.solution = verdict
            elif not problem.is_goal(node.state):
                self.solution = "Returned node is not a goal state"
        self.numNodeGenerated = SearchNode.node_count

    def __str__(self):
        message = f"{self.strategy_name}"
        message += f"\nSteps: {self.numSteps}, Cost: {self.totalWeight}, Node: {self.numNodeGenerated}"
        message += f", Time (ms): {int(self.time*1000)}, Memory (MB): {self.memory:.2f}"
        message += f"\n{self.solution}"
        return message
    
    def __json__(self):
        return {
            "strategy_name": self.strategy_name,
            "numSteps": int(self.numSteps),
            "totalWeight": int(self.totalWeight),
            "numNodeGenerated": int(self.numNodeGenerated),
            "time": self.time,
            "memory": self.memory,
            "solution": self.solution,
            "has_solution": self.has_solution
        }