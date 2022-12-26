# command = input()
# final_list = [0] * 10
#
# while command != "End":
#     command_list = command.split("-")
#     importance = int(command_list[0])
#     action = command_list[1]
#     final_list.pop(importance)
#     final_list.insert(importance, action)
#     command = input()
# result = [element for element in final_list if element != 0]
# print(result)

command = input()
sorted_list = [0] * 10

while command != "End":
    current_list = command.split("-")
    importance = int(current_list[0])
    action = current_list[1]
    sorted_list.pop(importance)
    sorted_list.insert(importance, action)

    command = input()

sorted_list = [element for element in sorted_list if element != 0]
print(sorted_list)