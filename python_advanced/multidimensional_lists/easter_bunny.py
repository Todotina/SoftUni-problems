size = int(input())
matrix = []
eggs_right = 0
eggs_left = 0
eggs_up = 0
eggs_down = 0
matrix_right = []
matrix_left = []
matrix_up = []
matrix_down = []
eggs_list = []
direction = ''
for _ in range(size):
    current_row = [x for x in input().split()]
    matrix.append(current_row)
for row in range(size):
    for col in range(size):
        if matrix[row][col] == "B":
            for index in range(1, abs(size - col)):
                if matrix[row][col + index] != "X":
                    direction = "right"
                    eggs_right += int(matrix[row][col + index])
                    matrix_right.append([row, col + index])
                else:
                    break
            eggs_list.append(eggs_right)
            for index in range(col -1, 0, -1):
                if matrix[row][index] != "X":
                    direction = "left"
                    eggs_left += int(matrix[row][index])
                    matrix_left.append([row, index])
                else:
                    break
            eggs_list.append(eggs_left)
            for index in range(1, abs(size - row)):
                if matrix[row + index][col] != "X":
                    direction = "down"
                    eggs_down += int(matrix[row+index][col])

                    matrix_down.append([row + index, col])
                else:
                    break
            eggs_list.append(eggs_down)
            for index in range(row-1, 0, -1):
                if matrix[index][col] != "X":
                    direction = "up"
                    eggs_up += int(matrix[index][col])

                    matrix_up.append([index, col])
                else:
                    break
            eggs_list.append(eggs_up)
            break
        else:
            continue

max_index = eggs_list.index(max(eggs_list))
if max_index == 0:
    print("right")
    for element in matrix_right:
        print(element)
    print(eggs_right)
elif max_index == 1:
    print("left")
    for element in matrix_left:
        print(element)
    print(eggs_left)
elif max_index == 2:
    print("down")
    for element in matrix_down:
        print(element)
    print(eggs_down)
elif max_index == 3:
    print("up")
    for element in matrix_up:
        print(element)
    print(eggs_up)