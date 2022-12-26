# def merge(start_index, end_index):
#     merged_items = ''.join(list_of_strings[start_index:end_index + 1])
#     list_of_strings[start_index:end_index + 1] = [merged_items]
#     return list_of_strings
#
# def divide(index, partitions):
#     length = list_of_strings[index] // partitions
#     if length * partitions > len(list_of_strings[index]):
#         pass
#     else:
#
#     # Every time you receive the divide command, you must divide the element at the given index into several small substrings
#     # with equal length.The count of the substrings should be equal to the given partitions.
#
# def index_validation(start_index, end_index):
#     if 0 <= start_index <= len(list_of_strings) and 0 < end_index <= len(list_of_strings):
#         merge(start_index,end_index)
#     else:
#         if start_index < len(list_of_strings):
#             start_index = start_index
#         if end_index > len(list_of_strings) - 1:
#             end_index = len(list_of_strings) - 1
#
#
# list_of_strings = input().split(" ")
# merged_items = ""
# command = input()
# while command != "3:1":
#     current_command_list = command.split(" ")
#     action = current_command_list[0]
#     start_index, index = current_command_list[1]
#     end_index, partitions = current_command_list[2]
#     if action == "merge":
#         merge(start_index, end_index)
#
#
#     command = input()
# if command == "3:1":
#     print(' '.join(list_of_strings))



