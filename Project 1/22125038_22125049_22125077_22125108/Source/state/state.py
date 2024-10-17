WALL = '#'
EMPTY = ' '
STONE = '$'
AGENT = '@'
SWITCH = '.'
STONE_SWITCH = '*'
AGENT_SWITCH = '+'

class Cell:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return self.value
    
class Stone(Cell):
    def __init__(self, weight: int):
        super().__init__(STONE)
        self.weight = weight

class SearchState:
    def __init__(self, file_input: str):
        self.state = None
        self.parse_input(file_input)

    def parse_input(self, file_input: str):
        with open(file_input, 'r') as f:
            lines = f.readlines()
            weights = list(map(int, lines[0].split()))
            def toCell(char):
                if char != STONE:
                    return Cell(char)
                else:
                    return Stone(weights.pop(0))
            self.state = [list(map(toCell, line[:-1])) for line in lines][1:]

    def __str__(self):
        weights = []
        for row in self.state:
            for cell in row:
                if str(cell) == STONE:
                    weights.append(cell.weight)
        string = ''
        string += str(weights) + '\n'
        string += '\n'.join([''.join([str(cell) for cell in row]) for row in self.state])
        return string