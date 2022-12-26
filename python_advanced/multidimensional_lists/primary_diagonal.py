size = int(input())
primary_diagonal = 0
for row in range(size):
    current_row = [int(x) for x in input().split()]
    primary_diagonal += current_row[row]
print(primary_diagonal)
