# text = input()
# list_of_characters_text = []
# for character in text:
#     list_of_characters_text.append(character)
# vowels_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
# for element in list_of_characters_text:
#     if element in vowels_list:
#         list_of_characters_text.remove(element)
# print("".join(list_of_characters_text))

text = input()
vowels_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
result = [character for character in text if character not in vowels_list]
print("".join(result))