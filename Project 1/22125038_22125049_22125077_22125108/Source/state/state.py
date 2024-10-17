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
            self.state = [list(line.strip()) for line in lines]

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.state])