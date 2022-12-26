size = int(input())
primary = []
secondary = []
for row in range(size):
    current_row = [int(x) for x in input().split(", ")]
    primary.append(current_row[row])
    index = - row - 1
    secondary.append(current_row[index])
print(f'Primary diagonal: {", ".join(str(element) for element in primary)}. Sum: {sum(primary)}')
print(f'Secondary diagonal: {", ".join(str(element) for element in secondary)}. Sum: {sum(secondary)}')