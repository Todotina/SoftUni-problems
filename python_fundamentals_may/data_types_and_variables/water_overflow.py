number_of_lines = int(input())
capacity = 255
filled_capacity = 0
for liters in range(number_of_lines):
    current_liters = int(input())
    filled_capacity += current_liters
    if filled_capacity > capacity:
        print("Insufficient capacity!")
        filled_capacity -= current_liters
        continue
print(f'{filled_capacity}')
