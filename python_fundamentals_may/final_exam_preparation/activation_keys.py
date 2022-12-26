def contains_substring(raw_activation_key, substring):
    if substring in raw_activation_key:
        print(f"{raw_activation_key} contains {substring}")
    else:
        print("Substring not found!")


def change_case(raw_activation_key, start_index, end_index):
    if case == "Upper":
        beginning = raw_activation_key[:start_index]
        change_to_upper = raw_activation_key[start_index:end_index].upper()
        end = raw_activation_key[end_index:]
        modified_key = beginning + change_to_upper + end
        modified_keys.append(modified_key)
        print(modified_key)
    elif case == "Lower":
        beginning = raw_activation_key[:start_index]
        change_to_lower = raw_activation_key[start_index:end_index].lower()
        end = raw_activation_key[end_index:]
        modified_key = beginning + change_to_lower + end
        modified_keys.append(modified_key)
        print(modified_key)


def slice_string(raw_activation_key, start_index, end_index):
    modified_key = raw_activation_key.replace(raw_activation_key[start_index:end_index], "")
    modified_keys.append(modified_key)
    print(modified_key)


raw_activation_key = input()
modified_keys = [raw_activation_key]
command = input()
while command != "Generate":
    current_instruction = command.split(">>>")
    action = current_instruction[0]
    if action == "Contains":
        substring = current_instruction[1]
        contains_substring(modified_keys[-1], substring)
    elif action == "Flip":
        case = current_instruction[1]
        start_index = int(current_instruction[2])
        end_index = int(current_instruction[3])
        change_case(modified_keys[-1], start_index, end_index)
    elif action == "Slice":
        start_index = int(current_instruction[1])
        end_index = int(current_instruction[2])
        slice_string(modified_keys[-1], start_index, end_index)

    command = input()


print(f"Your activation key is: {modified_keys[-1]}")
