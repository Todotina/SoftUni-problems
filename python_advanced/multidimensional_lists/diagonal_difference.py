size = int(input())
primary = []
secondary = []
for row in range(size):
    current_row = [int(x) for x in input().split()]
    primary.append(current_row[row])
    index = - row - 1
    secondary.append(current_row[index])
difference = abs(sum(primary) - sum(secondary))
print(difference)