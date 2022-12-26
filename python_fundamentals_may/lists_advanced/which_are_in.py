first_input = input().split(', ')
second_input = input().split(', ')
# final_list = [element for element in first_input if any(element in word for word in second_input)]
final_list = []
for first_word in first_input:
    for second_word in second_input:
        if first_word in second_word and not first_word in final_list:
            final_list.append(first_word)
            break
print(final_list)
