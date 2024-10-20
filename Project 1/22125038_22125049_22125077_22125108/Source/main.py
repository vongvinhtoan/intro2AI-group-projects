from problem import *
from strategy import *

def parse_args():
    import argparse
    return {
        'strategies': ['DFS', 'BFS', 'UCS', 'A*'],
        'input_files': ['input-01.txt', 'input-02.txt'],
        'output_files': ['output-01.txt', 'output-02.txt']
    }

def main():
    args = parse_args()
    strategies = args['strategies']
    input_files = args['input_files']
    output_files = args['output_files']

    solvers = [solver_dict[strategy] for strategy in strategies]

    def file_streams(input_files, output_files):
        for input_file, output_file in zip(input_files, output_files):
            input_stream = open(input_file, 'r')
            output_stream = open(output_file, 'w')
            yield input_stream, output_stream, input_file, output_file
    
    for input_stream, output_stream, input_file, output_file in file_streams(input_files, output_files):
        print()
        print(f"Processing {input_file} ---> {output_file}...")
        print()
        problem = Problem()
        problem.parse_input(input_stream)

        for solver in solvers:
            output = solver.solve(problem)
            output_stream.write(str(output) + '\n')


if __name__ == '__main__':
    main()