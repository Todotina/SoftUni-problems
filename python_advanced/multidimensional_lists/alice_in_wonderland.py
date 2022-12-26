size = int(input())
matrix =[]
for _ in range(size):
    current_row = input().split()
    matrix.append(current_row)
tea_bags = 0
c_row = 0
c_col = 0
for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'A':
            matrix[row][col] = "*"
            c_row = row
            c_col = col
            break
        else:
            continue

command = input()
while command:
    if command == "down":
        if c_row + 1 <= size - 1:
            if matrix[c_row + 1][c_col] != "." and matrix[c_row + 1][c_col] != "*" and matrix[c_row + 1][c_col] != "R":
                tea_bags += int(matrix[c_row + 1][c_col])
            elif matrix[c_row + 1][c_col] == "R":
                matrix[c_row + 1][c_col] = "*"
                print("Alice didn't make it to the tea party.")
                for item in matrix:
                    print(f'{" ".join(str(x) for x in item)}')
                break
            matrix[c_row + 1][c_col] = "*"
            c_row = c_row + 1
        else:
            print("Alice didn't make it to the tea party.")
            for item in matrix:
                print(f'{" ".join(str(x) for x in item)}')
            break
    elif command == "right":
        if c_col + 1 <= size - 1:
            if matrix[c_row][c_col+1] != "." and matrix[c_row][c_col+1] != "*" and matrix[c_row][c_col+1] != "R":
                tea_bags += int(matrix[c_row][c_col+1])
            elif matrix[c_row][c_col+1] == "R":
                matrix[c_row][c_col + 1] = "*"
                print("Alice didn't make it to the tea party.")
                for item in matrix:
                    print(f'{" ".join(str(x) for x in item)}')
                break
            matrix[c_row][c_col + 1] = "*"
            c_col = c_col + 1
        else:
            print("Alice didn't make it to the tea party.")
            for item in matrix:
                print(f'{" ".join(str(x) for x in item)}')
            break
    elif command == "up":
        if c_row - 1 >= 0:
            if matrix[c_row - 1][c_col] != "." and matrix[c_row - 1][c_col] != "*" and matrix[c_row - 1][c_col] != "R":
                tea_bags += int(matrix[c_row - 1][c_col])
            elif matrix[c_row - 1][c_col] == "R":
                matrix[c_row - 1][c_col] = "*"
                print("Alice didn't make it to the tea party.")
                for item in matrix:
                    print(f'{" ".join(str(x) for x in item)}')
                break
            matrix[c_row - 1][c_col] = "*"
            c_row = c_row - 1
        else:
            print("Alice didn't make it to the tea party.")
            for item in matrix:
                print(f'{" ".join(str(x) for x in item)}')
            break
    elif command == "left":
        if c_col - 1 >= 0:
            if matrix[c_row][c_col-1] != "." and matrix[c_row][c_col-1] != "*" and matrix[c_row][c_col-1] != "R":
                tea_bags += int(matrix[c_row][c_col-1])
            elif matrix[c_row][c_col-1] == "R":
                matrix[c_row][c_col - 1] = "*"
                print("Alice didn't make it to the tea party.")
                for item in matrix:
                    print(f'{" ".join(str(x) for x in item)}')
                break
            matrix[c_row][c_col-1] = "*"
            c_col = c_col - 1
        else:
            print("Alice didn't make it to the tea party.")
            for item in matrix:
                print(f'{" ".join(str(x) for x in item)}')
            break
    command = input()

if tea_bags >= 10:
    print("She did it! She went to the party.")
    for item in matrix:
        print(f'{" ".join(str(x) for x in item)}')