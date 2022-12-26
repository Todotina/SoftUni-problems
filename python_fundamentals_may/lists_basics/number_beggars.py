# list_of_integers_strings = input(). split(", ")
# count_beggars = int(input())
# list_of_integers_numbers = []
# final_list = []
# counter_of_index = 0
# for element in list_of_integers_strings:
#     list_of_integers_numbers.append(int(element))
# while counter_of_index < count_beggars:
#     sum_for_current_beggar = 0
#     for current_index in range(counter_of_index, len(list_of_integers_numbers), count_beggars):
#         sum_for_current_beggar += list_of_integers_numbers[current_index]
#     counter_of_index += 1
#     final_list.append(sum_for_current_beggar)
# print(final_list)

list_integers = input().split(", ")
number_of_beggars = int(input())
list_sums = []
for beggar in range(1, number_of_beggars + 1):
    sum_current_beggar = 0
    for index in range(0, len(list_integers), number_of_beggars):
        sum_current_beggar += int(list_integers[index])
    list_sums.append(sum_current_beggar)
print(list_sums)
