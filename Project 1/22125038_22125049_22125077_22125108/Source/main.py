from problem import *
from strategy import *
from utils import parse_args
import exrex, re
import json

def run_solver(args):
    strategies = args['strat']
    input_files = args['in']
    output_files = args['out']
    solution_files = args['sol']
    input_regex = args['inregex']
    output_regex = args['outregex']
    solution_regex = args['solregex']
    time_limit = args['time_limit']
    memory_limit = args['memory_limit']

    solvers = [solver for name, solver in solver_dict.items() if re.fullmatch('|'.join(strategies), name)]

    def file_streams():
        if input_files is not None and output_files is not None and solution_files is not None:
            for input_file, output_file, solution_file in zip(input_files, output_files, solution_files):
                input_stream = open(input_file, 'r')
                output_stream = open(output_file, 'w')
                solution_stream = open(solution_file, 'w')
                yield input_stream, output_stream, solution_stream
        elif input_regex is not None and output_regex is not None and solution_regex is not None:
            for input_file, output_file, solution_file in zip(exrex.generate(input_regex), exrex.generate(output_regex), exrex.generate(solution_regex)):
                if not re.fullmatch(input_regex, input_file) or not re.fullmatch(output_regex, output_file) or not re.fullmatch(solution_regex, solution_file):
                    continue
                input_stream = open(input_file, 'r')
                output_stream = open(output_file, 'w')
                solution_stream = open(solution_file, 'w')
                yield input_stream, output_stream, solution_stream
        else:
            raise ValueError("Invalid input/output/solution files or regex")
    
    for input_stream, output_stream, solution_stream in file_streams():
        print()
        print(f"Processing {input_stream.name} ---> {output_stream.name}...")
        print()
        problem = Problem()
        problem.parse_input(input_stream)

        result_list = []
        for solver in solvers:
            output = solver.solve(problem, time_limit, memory_limit)
            output_stream.write(str(output) + '\n')
            result_list.append(output.__json__())
        solution_stream.write(json.dumps(result_list, indent=4))

def main():
    args = parse_args()
    if args['file'] is None:
        run_solver(args)
    else:
        with open(args['file'], 'r') as f:
            for line in f:
                args = parse_args(line.split())
                run_solver(args)


if __name__ == '__main__':
    main()