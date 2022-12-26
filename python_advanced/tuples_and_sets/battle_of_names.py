number = int(input())
odd_set = set()
even_set = set()
for item in range(1, number+1):
    current_name = input()
    current_sum = 0
    for letter in current_name:
        current_sum += ord(letter)
    final_value = current_sum//item
    if final_value % 2 == 0:
        even_set.add(final_value)
    else:
        odd_set.add(final_value)
odd_sum = sum(odd_set)
even_sum = sum(even_set)
if odd_sum == even_sum:
    union = ', '.join(str(item) for item in odd_set and even_set)
    print(f'{union}')
elif odd_sum > even_sum:
    odd_string = ', '.join(str(item) for item in odd_set)
    print(f'{odd_string}')
elif odd_sum < even_sum:
    symmetric_difference = ', '.join(str(item) for item in odd_set if item not in even_set and str(item) for item in even_set if item not in odd_set)
    print(f'{symmetric_difference}')