from state import *
from strategy import *

def parse_args():
    import argparse
    return {
        'strategies': ['DFS', 'BFS', 'UCS', 'A*'],
        'input_files': ['input-01.txt'],
        'output_files': ['output-01.txt']
    }

def main():
    args = parse_args()
    strategies = args['strategies']
    input_files = args['input_files']
    output_files = args['output_files']

    solvers = [solver_dict[strategy] for strategy in strategies]
    
    for input_file, output_file in zip(input_files, output_files):
        state = SearchState(input_file)

        # Clear the output file
        open(output_file, 'w').close()

        for solver in solvers:
            solver.set_state(state)
            output = solver.search()
            output.write(output_file)

if __name__ == '__main__':
    main()