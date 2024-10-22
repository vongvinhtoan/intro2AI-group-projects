from problem import *
from strategy import *
from utils import parse_args
import exrex, re

def main():
    args = parse_args()
    strategies = args['strat']
    input_files = args['in']
    output_files = args['out']
    input_regex = args['inregex']
    output_regex = args['outregex']

    print(list(exrex.generate('a[1-3]b')))

    solvers = [solver for name, solver in solver_dict.items() if re.fullmatch('|'.join(strategies), name)]

    def file_streams():
        if input_files is not None and output_files is not None:
            for input_file, output_file in zip(input_files, output_files):
                input_stream = open(input_file, 'r')
                output_stream = open(output_file, 'w')
                yield input_stream, output_stream
        if input_regex is not None and output_regex is not None: 
            print(input_regex, output_regex)
            for input_file, output_file in zip(exrex.generate(input_regex), exrex.generate(output_regex)):
                print(input_file, output_file)
                input_stream = open(input_file, 'r')
                output_stream = open(output_file, 'w')
                yield input_stream, output_stream
    
    for input_stream, output_stream in file_streams():
        print()
        print(f"Processing {input_stream.name} ---> {output_stream.name}...")
        print()
        problem = Problem()
        problem.parse_input(input_stream)

        for solver in solvers:
            output = solver.solve(problem)
            output_stream.write(str(output) + '\n')


if __name__ == '__main__':
    main()