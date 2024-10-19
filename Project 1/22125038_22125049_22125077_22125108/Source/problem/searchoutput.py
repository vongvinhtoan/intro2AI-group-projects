class SearchOutput:
    def __init__(self, strategy_name: str):
        self.strategy_name = strategy_name
        self.numSteps = 0
        self.totalWeight = 0
        self.numNodeGenerated = 0
        self.time = 0
        self.memory = 0
        self.solution = ""

    def commit(self, solution: str, totalWeight: int):
        self.numSteps = len(solution)
        self.totalWeight = totalWeight
        self.solution = solution

    def __str__(self):
        message = f"{self.strategy_name}"
        message += f"\nSteps: {self.numSteps}, Weight: {self.totalWeight}, Node: {self.numNodeGenerated}"
        message += f", Time (ms): {self.time:.2f}, Memory (MB): {self.memory:.2f}"
        message += f"\n{self.solution}"
        return message