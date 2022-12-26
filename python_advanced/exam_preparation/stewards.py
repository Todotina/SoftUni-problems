from collections import deque

seats = input().split(", ")
first_numbers = deque([int(x) for x in input().split(", ")])
second_numbers = deque([int(x) for x in input().split(", ")])

rotations = 0
seat_matches = []

while True:
    current_sum = first_numbers[0] + second_numbers[-1]
    current_character = chr(current_sum)
    first_option = str(first_numbers[0]) + current_character
    second_option = str(second_numbers[-1]) + current_character
    if first_option in seats:
        if first_option not in seat_matches:
            seat_matches.append(first_option)
        rotations += 1
        first_numbers.popleft()
        second_numbers.pop()
    elif second_option in seats:
        if second_option not in seat_matches:
            seat_matches.append(second_option)
        rotations += 1
        first_numbers.popleft()
        second_numbers.pop()
    else:
        rotations += 1
        first_numbers.append(first_numbers.popleft())
        second_numbers.appendleft(second_numbers.pop())
    if len(seat_matches) >= 3 or rotations >= 10:
        break

print(f'Seat matches: {", ".join(str(x) for x in seat_matches)}')
print(f'Rotations count: {rotations}')


