import sys

count_numbers = int(input())
max_number = - sys.maxsize
sum= 0

for numbers in range(1, count_numbers + 1):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    sum = sum + current_number
sum = sum - max_number
if max_number == sum:
    print("Yes")
    print(f"Sum = {sum}")
else:
    print("No")
    print(f"Diff = {abs(max_number - sum)}")