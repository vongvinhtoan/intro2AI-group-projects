import argparse

def parse_args(args=None):
    parser = argparse.ArgumentParser(description='Solve a given problem with a given strategy.')
    parser.add_argument('--strat', '-s', nargs='+', type=str, help='List of strategies to use', default="")
    parser.add_argument('--in', '-i', nargs='+', type=str, help='List of input files', default=None)
    parser.add_argument('--out', '-o', nargs='+', type=str, help='List of output files', default=None)
    parser.add_argument('--sol', '-so', nargs='+', type=str, help='List of solution files', default=None)
    parser.add_argument('--inregex', '-ir', type=str, help='Regex for input files', default=None)
    parser.add_argument('--outregex', '-or', type=str, help='Regex for output files', default=None)
    parser.add_argument('--solregex', '-sor', type=str, help='Regex for solution files', default=None)
    parser.add_argument('--time_limit', '-TL', type=int, help='Time limit for each strategy', default=-1)
    parser.add_argument('--memory_limit', '-ML', type=int, help='Memory limit for each strategy', default=-1)
    parser.add_argument('--file', '-f', type=str, help='File to read arguments from', default=None)
    if args is not None:
        return vars(parser.parse_args(args))
    return vars(parser.parse_args())