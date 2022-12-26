count_of_numbers = int(input())
first_number = int(input())
largest_number = first_number
smallest_number = first_number

for numbers in range(count_of_numbers - 1):
    current_number = int(input())
    if current_number < smallest_number:
        smallest_number = current_number
    if current_number > largest_number:
        largest_number = current_number
print(f"Max number: {largest_number}")
print(f"Min number: {smallest_number}")