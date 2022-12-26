n = int(input())
current_number = 0
is_current_bigger_than_n = False
for rows in range(1, n+1):
    for columns in range(1, rows+1):
        current_number += 1
        if current_number > n:
            is_current_bigger_than_n = True
            break
        print(current_number, end=' ')
    if is_current_bigger_than_n == True:
        break
    print()