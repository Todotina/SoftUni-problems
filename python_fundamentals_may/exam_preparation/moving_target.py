targets_list = [int(number) for number in input().split(" ")]
command = input()
valid_index = False
while command != "End":
    current_action = command.split(" ")
    current_index = int(current_action[1])
    if 0 <= current_index < len(targets_list):
        valid_index = True
    if current_action[0] == "Shoot" and valid_index:
        current_power = int(current_action[2])
        remaining_value_target = targets_list[current_index] - current_power
        if remaining_value_target <= 0:
            targets_list.remove(targets_list[current_index])
        else:
            targets_list[current_index] = remaining_value_target
    elif current_action[0] == "Strike":
        current_radius = int(current_action[2])
        left_side = targets_list[:current_index]
        right_side = targets_list[current_index + 1:]
        if current_radius <= len(left_side) and current_radius <= len(right_side) and valid_index:
            for index in range(current_index - current_radius, current_index + current_radius + 1):
                targets_list[index] = 0
        else:
            print("Strike missed!")
        targets_list = [number for number in targets_list if number != 0]
    elif current_action[0] == "Add":
        if valid_index:
            current_value = int(current_action[2])
            targets_list.insert(current_index, current_value)
        else:
            print("Invalid placement!")
    valid_index = False
    command = input()
if command == "End":
    print(f"{'|'.join(map(str, targets_list))}")


# def is_index_valid(targets, index):
#     if 0 <= int(index) < len(targets):
#         return True
#     return False
#
#
# def shoot_function(targets, command):
#     action, index, power = command.split()
#     index = int(index)
#     power = int(power)
#     if is_index_valid(targets, index):
#         targets[index] -= power
#         if int(targets[index]) <= 0:
#             targets.remove(targets[index])
#     return targets
#
#
# def add_function(targets, command):
#     action, index, value = command.split()
#     index = int(index)
#     value = int(value)
#     if is_index_valid(targets, index):
#         targets.insert(index, value)
#         return targets
#     print("Invalid placement!")
#
#
# def strike_function(targets, command):
#     action, index, radius = command.split()
#     index = int(index)
#     radius = int(radius)
#     left_side = targets[:index]
#     right_side = targets[index + 1:]
#     if radius <= len(left_side) and radius <= len(right_side) and is_index_valid(targets, index):
#         for num in range(radius):
#             left_side.remove(left_side[-1])
#             right_side.pop(0)
#         targets.clear()
#         targets += left_side + right_side
#         return targets
#     else:
#         print('Strike missed!')
#
#
# targets = list(map(int, input().split()))
# command = input()
#
# while not command == 'End':
#     if 'Shoot' in command:
#         shoot_function(targets, command)
#     elif 'Strike' in command:
#         strike_function(targets, command)
#     elif 'Add' in command:
#         add_function(targets, command)
#     command = input()
#
# targets = ('|'.join(str(el) for el in targets))
# print(targets)