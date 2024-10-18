import state

class Problem:
    class Action:
        def __init__(self, name, direction, needPush):
            self.name = name
            self.direction = direction
            self.needPush = needPush

        def __str__(self):
            return f"Action: {self.name}, Direction: {self.direction}, NeedPush: {self.needPush}"

    def __init__(self, initialState: state.SearchState):
        self.initialState = initialState

        self.mapHeight = initialState.state.shape[0]
        self.mapWidth = initialState.state.shape[1]
        
        self.switchPositions = []
        for row in range(self.mapHeight):
            for col in range(self.mapWidth):
                if state.cellType(initialState.state[row,col]) in (state.SWITCH, state.AGENT_SWITCH, state.STONE_SWITCH):
                    self.switchPositions.append((row,col))

    def isGoal(self, s: state.SearchState):
        for switch in self.switchPositions:
            if state.cellType(s.state[switch]) != state.STONE_SWITCH:
                return False
        return True

    def __valid_move(self, s: state.SearchState, direction):
        def __valid_pos(pos):
            return pos[0] in range(self.mapHeight) and pos[1] in range(self.mapWidth)

        newPos = (s.agentPosition[0] + direction[0], s.agentPosition[1] + direction[1])

        # Check if new position is within the board
        if not __valid_pos(newPos):
            return False, None
        
        # Check if new position is not wall
        if state.cellType(s.state[newPos]) == state.WALL:
            return False, None
        
        # Check if new position has stone and stone can be pushed
        needPush = False
        if state.cellType(s.state[newPos]) in (state.STONE, state.STONE_SWITCH): 
            newStonePos = (newPos[0] + direction[0], newPos[1] + direction[1])
            if not __valid_pos(newStonePos) or state.cellType(s.state[newStonePos]) not in (state.EMPTY, state.SWITCH):
                return False, None
            needPush = True

        return True, needPush

    def actions(self, s: state.SearchState):
        actions = []
        for direction in state.agent_directions:
            valid, needPush = self.__valid_move(s, state.agent_directions[direction])
            if valid:
                actions.append(self.Action(direction, state.agent_directions[direction], needPush))
        return actions
    
    def result(self, s: state.SearchState, a: Action):
        newState = s.state.copy()
        newAgentPos = (s.agentPosition[0] + a.direction[0], s.agentPosition[1] + a.direction[1])

        print(f"Agent Position: {s.agentPosition}, New Agent Position: {newAgentPos}")

        cost = 1
        if a.needPush:
            stoneWeight = state.weight(newState[newAgentPos])
            cost += stoneWeight
            newStonePos = (newAgentPos[0] + a.direction[0], newAgentPos[1] + a.direction[1])
            newState[newStonePos] = state.addStone(newState[newStonePos], stoneWeight)
            newState[newAgentPos] = state.removeStone(newState[newAgentPos])

        newState[newAgentPos] = state.addAgent(newState[newAgentPos])
        newState[s.agentPosition] = state.removeAgent(newState[s.agentPosition])

        return state.SearchState(newState), cost