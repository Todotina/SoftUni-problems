def cheating(first_index, second_index):
    if first_index == second_index or not 0 <= first_index < len(list_of_elements) or not 0 <= second_index < len(
            list_of_elements):
        print("Invalid input! Adding additional elements to the board")
        middle = len(list_of_elements) // 2
        elements_to_insert = "-2a"
        list_of_elements.insert(middle, elements_to_insert)
        list_of_elements.insert(middle, elements_to_insert)
        return False
    else:
        return True


def matching_elements(first_index, second_index):
    if list_of_elements[first_index] == list_of_elements[second_index]:
        print(f"Congrats! You have found matching elements - {list_of_elements[first_index]}!")
        return True
    else:
        print("Try again!")
        return False


list_of_elements = input().split()
current_sequence = []
command = input()
same_elements = 0
number_of_moves = 0
while command != "end":
    number_of_moves += 1
    list_current_indexes = [int(number) for number in command.split()]
    # cheating(list_current_indexes[0], list_current_indexes[1])
    if not cheating(list_current_indexes[0], list_current_indexes[1]):
        command = input()
        continue
    # matching_elements(list_current_indexes[0], list_current_indexes[1])
    if matching_elements(list_current_indexes[0], list_current_indexes[1]):
        same_elements += 1
        list_of_elements[list_current_indexes[0]] = 0
        list_of_elements[list_current_indexes[1]] = 0
        list_of_elements = [number for number in list_of_elements if number != 0]

    if len(list_of_elements) == 0:
        print(f"You have won in {number_of_moves} turns!")
        break

    command = input()

if command == "end" and len(list_of_elements) > 0:
    print("Sorry you lose :(")
    print(' '.join(list_of_elements))