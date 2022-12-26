initial_array = [int(number) for number in input().split(" ")]
command = input()
final_array = []

while command != "end" and command != "decrease":
    list_current_action = [element for element in command.split(" ")]
    action = list_current_action[0]
    index_one = int(list_current_action[1])
    index_two = int(list_current_action[2])
    if action == "swap":
        initial_array[index_one], initial_array[index_two] = initial_array[index_two], initial_array[index_one]
    elif action == "multiply":
        product = initial_array[index_one] * initial_array[index_two]
        del initial_array[1]
        initial_array.insert(1, product)

    command = input()

if command == "decrease":
    for element in initial_array:
        element -= 1
        final_array.append(element)

print(', '.join(map(str, final_array)))


