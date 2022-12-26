first_number = int(input())
second_number = int(input())

for number in range(first_number, second_number + 1):
    current_number_string = str(number)
    even_sum = 0
    odd_sum = 0
    for position in range(0, 6):
        current_position_number = int(current_number_string[position])
        if position % 2 == 0:
            even_sum += current_position_number
        else:
            odd_sum += current_position_number
    if odd_sum == even_sum:
        print(number, end= " ")