rows, cols = [int(x) for x in input().split()]
matrix = []
sub_matrix = []
for row in range(rows):
    for col in range(cols):
        current_sequence = chr(97+row) + chr(97 + col+row) + chr(97+row)
        sub_matrix.append(current_sequence)
    matrix.append(sub_matrix)
    sub_matrix = []
for element in matrix:
    print(f'{" ".join([x for x in element])}')