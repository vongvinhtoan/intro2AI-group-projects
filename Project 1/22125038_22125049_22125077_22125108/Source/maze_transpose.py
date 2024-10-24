def transpose_maze(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    matrix = [list(line.rstrip('\n')) for line in lines]

    transposed_matrix = list(map(list, zip(*matrix)))

    transposed_lines = [''.join(row) for row in transposed_matrix]

    with open(output_file, 'w') as f:
        f.write('\n'.join(transposed_lines))

if __name__ == '__main__':
    transpose_maze('input-07.txt', 'output-07.txt')