integers = input().split(" ")
targets_list = [int(number) for number in integers]
command = input()
shot_targets = 0
final_list = []
while command != "End":
    current_index = int(command)
    if 0 <= current_index < len(targets_list):
        value_current_target = targets_list[current_index]
        targets_list[current_index] = -1
        shot_targets += 1
        for number in targets_list:
            if number == -1:
                number += 0
            elif number > value_current_target:
                number -= value_current_target
            elif number <= value_current_target:
                number += value_current_target
            final_list.append(number)
        targets_list = final_list.copy()
        final_list.clear()
    command = input()
if command == "End":
    print(f"Shot targets: {shot_targets} -> {' '.join(map(str, targets_list))}")