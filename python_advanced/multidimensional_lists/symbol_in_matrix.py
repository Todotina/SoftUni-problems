size = int(input())
matrix = []

for row in range(size):
    current_row = input()
    matrix.append(current_row)
symbol = input()
symbol_present = False
for row in range(size):
    for col in range(size):
        current_symbol = matrix[row][col]
        if symbol == current_symbol:
            print(f"({row}, {col})")
            symbol_present = True
            break
    if symbol_present:
        break
if not symbol_present:
    print(f"{symbol} does not occur in the matrix")
