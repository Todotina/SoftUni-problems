# count_of_numbers = int(input())
# left_sum = 0
# right_sum = 0
# for numbers in range(2 * count_of_numbers):
#     current_number = int(input())
#     if numbers < count_of_numbers:
#         left_sum += current_number
#     else:
#         right_sum += current_number
# if left_sum == right_sum:
#     print(f'Yes, sum = {left_sum}')
# else:
#     print(f'No, diff = {abs(left_sum - right_sum)}')

count_of_numbers = int(input())
left_sum = 0
for numbers in range(1, count_of_numbers + 1):
    current_number = int(input())
    left_sum = left_sum + current_number
right_sum = 0
for numbers in range(1, count_of_numbers + 1):
    current_number = int(input())
    right_sum = right_sum + current_number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(right_sum - left_sum)
    print(f"No, diff = {diff}")