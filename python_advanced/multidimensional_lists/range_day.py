matrix = []
for _ in range(5):
    current_row = input().split()
    matrix.append(current_row)
c_row = 0
c_col = 0
total_targets = 0
shot_targets = 0
for row in range(5):
    for col in range(5):
        if matrix[row][col] == "A":
            c_row = row
            c_col = col
        elif matrix[row][col] == "x":
            total_targets += 1

indexes = []
commands = int(input())
for command in range(commands):
    current_command = input().split()
    if current_command[0] == "move":
        direction, steps = current_command[1], int(current_command[2])
        if direction == "right" and c_col+steps <= 4 and matrix[c_row][c_col + steps] == ".":
            c_col = c_col + steps
        elif direction == "down" and c_row+steps <= 4 and matrix[c_row+steps][c_col] == ".":
            c_row = c_row + steps
        elif direction == "up" and c_row - steps >= 0 and matrix[c_row - steps][c_col] == ".":
            c_row = c_row - steps
        elif direction == "left" and c_col - steps >= 0 and matrix[c_row][c_col - steps]:
            c_col = c_col - steps
    elif current_command[0] == "shoot":
        direction = current_command[1]
        if direction == "right":
            for position in range(c_col+1, 4+1):
                if matrix[c_row][position] == "x":
                    shot_targets += 1
                    matrix[c_row][position] = "."
                    indexes.append([c_row, position])
                    break
        elif direction == "down":
            for position in range(c_row+1, 4+1):
                if matrix[position][c_col] == "x":
                    shot_targets += 1
                    matrix[position][c_col] = "."
                    indexes.append([position, c_col])
                    break
        elif direction == "up":
            for position in range(c_row-1, -1, -1):
                if matrix[position][c_col] == "x":
                    shot_targets += 1
                    matrix[position][c_col] = "."
                    indexes.append([position, c_col])
                    break
        elif direction == "left":
            for position in range(c_col-1, -1, -1):
                if matrix[c_row][position] == "x":
                    shot_targets += 1
                    matrix[c_row][position] = "."
                    indexes.append([c_row, position])
                    break
if shot_targets == total_targets:
    print(f"Training completed! All {shot_targets} targets hit.")
else:
    print(f"Training not completed! {total_targets-shot_targets} targets left.")
for item in indexes:
    print(item)