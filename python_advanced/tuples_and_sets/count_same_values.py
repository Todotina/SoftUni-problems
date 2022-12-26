numbers = tuple(input().split())
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

for item in unique_numbers:
    count = numbers.count(item)
    print(f'{float(item)} - {count} times')