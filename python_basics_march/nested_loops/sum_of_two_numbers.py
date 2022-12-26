first_number = int(input())
second_number = int(input())
magic_number = int(input())
count_combinations = 0
combination_is_found = False
for x1 in range(first_number, second_number+1):
    for x2 in range(first_number, second_number+1):
        count_combinations += 1
        if x1 + x2 == magic_number:
            combination_is_found = True
            break
    if combination_is_found == True:
        break
if combination_is_found:
    print(f"Combination N:{count_combinations} ({x1} + {x2} = {magic_number})")
else:
    print(f"{count_combinations} combinations - neither equals {magic_number}")