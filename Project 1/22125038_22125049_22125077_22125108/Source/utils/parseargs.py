import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Solve a given problem with a given strategy.')
    parser.add_argument('--strat', '-s', nargs='+', type=str, required=True, help='List of strategies to use')
    parser.add_argument('--in', '-i', nargs='+', type=str, help='List of input files', default=None)
    parser.add_argument('--out', '-o', nargs='+', type=str, help='List of output files', default=None)
    parser.add_argument('--inregex', '-ir', type=str, help='Regex for input files', default=None)
    parser.add_argument('--outregex', '-or', type=str, help='Regex for output files', default=None)
    return vars(parser.parse_args())