numbers = input().split("|")
matrix = []

for element in numbers:
    sub_matrix = []
    for item in element.split():
        if item != '':
            sub_matrix.append(item)
    matrix.append(sub_matrix)
reversed_matrix = []
[reversed_matrix.extend(element) for element in matrix[::-1]]
print(f'{" ".join(reversed_matrix)}')