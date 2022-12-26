number_of_people = int(input())
current_state = [int(number) for number in input().split(" ")]
people_left = number_of_people
final_state = []
total_free_spots = 0
for number in current_state:
    free_spots_current_wagon = 4 - number
    if people_left > free_spots_current_wagon:
        final_state.append(str(free_spots_current_wagon + number))
    else:
        final_state.append(str(people_left))
    people_left -= free_spots_current_wagon
    total_free_spots += free_spots_current_wagon
if total_free_spots > number_of_people:
    print("The lift has empty spots!")
    print(' '.join(final_state))
elif total_free_spots < number_of_people:
    print(f"There isn't enough space! {number_of_people-total_free_spots} people in a queue!")
    print(' '.join(final_state))
else:
    print(' '.join(final_state))

