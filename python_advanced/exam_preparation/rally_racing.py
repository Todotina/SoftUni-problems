size = int(input())
racing_number = input()
matrix = []
directions = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0)
}

tunnel = {}
for number in range(size):
    current_row = input().split()
    if "T" in current_row and len(tunnel) == 0:
        tunnel['first'] = (number, current_row.index("T"))
    elif "T" in current_row and len(tunnel) > 0:
        tunnel['second'] = (number, current_row.index("T"))
    matrix.append(current_row)

coordinates = (0, 0)
passed_km = 0

while True:
    command = input()
    if command == "left":
        row, col = coordinates[0] + directions['left'][0], coordinates[1] + directions['left'][1]
        if matrix[row][col] == ".":
            passed_km += 10
        elif matrix[row][col] == "T":
            matrix[row][col] = "."
            passed_km += 30
            row, col = tunnel['second']
            matrix[row][col] = "."
        elif matrix[row][col] == "F":
            matrix[row][col] = "C"
            passed_km += 10
            print(f"Racing car {racing_number} finished the stage!")
            print(f"Distance covered {passed_km} km.")
            break
        coordinates = (row, col)
    elif command == "right":
        row, col = coordinates[0] + directions['right'][0], coordinates[1] + directions['right'][1]
        if matrix[row][col] == ".":
            passed_km += 10
        elif matrix[row][col] == "T":
            matrix[row][col] = "."
            passed_km += 30
            row, col = tunnel['second']
            matrix[row][col] = "."
        elif matrix[row][col] == "F":
            matrix[row][col] = "C"
            passed_km += 10
            print(f"Racing car {racing_number} finished the stage!")
            print(f"Distance covered {passed_km} km.")
            break
        coordinates = (row, col)
    elif command == "up":
        row, col = coordinates[0] + directions['up'][0], coordinates[1] + directions['up'][1]
        if matrix[row][col] == ".":
            passed_km += 10
        elif matrix[row][col] == "T":
            matrix[row][col] = "."
            passed_km += 30
            row, col = tunnel['second']
            matrix[row][col] = "."
        elif matrix[row][col] == "F":
            matrix[row][col] = "C"
            passed_km += 10
            print(f"Racing car {racing_number} finished the stage!")
            print(f"Distance covered {passed_km} km.")
            break
        coordinates = (row, col)
    elif command == "down":
        row, col = coordinates[0] + directions['down'][0], coordinates[1] + directions['down'][1]
        if matrix[row][col] == ".":
            passed_km += 10
        elif matrix[row][col] == "T":
            matrix[row][col] = "."
            passed_km += 30
            row, col = tunnel['second']
            matrix[row][col] = "."
        elif matrix[row][col] == "F":
            matrix[row][col] = "C"
            passed_km += 10
            print(f"Racing car {racing_number} finished the stage!")
            print(f"Distance covered {passed_km} km.")
            break
        coordinates = (row, col)
    elif command == "End":
        matrix[coordinates[0]][coordinates[1]] = "C"
        print(f"Racing car {racing_number} DNF.")
        print(f"Distance covered {passed_km} km.")
        break

for row in matrix:
    print(f'{"".join(x for x in row)}')

