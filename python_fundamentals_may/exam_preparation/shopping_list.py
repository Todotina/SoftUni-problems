def existing_item(item):
    if item in shopping_list:
        return True
    else:
        return False


shopping_list = input().split("!")
command = input()
final_list = []
while command != "Go Shopping!":
    current_command_list = command.split(" ")
    action = current_command_list[0]
    item = current_command_list[1]
    if action == "Urgent" and not existing_item(item):
        shopping_list[0] = item
    elif action == "Unnecessary" and existing_item(item):
        shopping_list.remove(item)
    elif action == "Correct" and existing_item(item):
        index_item = shopping_list.index(item)
        shopping_list[index_item] = current_command_list[2]
    elif action == "Rearrange" and existing_item(item):
        index_item = shopping_list.index(item)
        shopping_list[index_item] = shopping_list[-1]

    command = input()

print(', '.join(shopping_list))

