number_of_lines = int(input())
total_sum = 0
for letter in range(1, number_of_lines + 1):
    current_letter = input()
    total_sum += ord(current_letter)
print(f"The sum equals: {total_sum}")