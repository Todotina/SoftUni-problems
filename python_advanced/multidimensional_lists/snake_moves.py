rows, cols = [int(x) for x in input().split()]
string = input()
# difference = len(string) - cols
matrix = []
ind = 0
for row in range(rows):
    new_string = ''
    for col in range(cols):
        new_string += string[ind % len(string)]
        ind += 1

    if row % 2 == 0:
        matrix.append(new_string)
    else:
        matrix.append(new_string[::-1])
# for row in range(rows):
#     if row == 0:
#         for col in range(cols):
#             new_string += string[col]
#         matrix.append(new_string)
#     elif row % 2 != 0:
#         for col in range(difference, 0, -1):
#             new_string += string[-col]
#         for col in range(cols - difference):
#             new_string += string[col]
#         backward_string = new_string[::-1]
#         matrix.append(backward_string)
#     else:
#         for col in range(difference + 1, 0, -1):
#             new_string += string[-col]
#         for col in range(cols - difference - 1):
#             new_string += string[col]
#         matrix.append(new_string)
#     new_string = ''
for element in matrix:
    print(element)