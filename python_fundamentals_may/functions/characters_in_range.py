def single_string(first_character, second_character):
    list_of_characters = []
    for character in range(ord(first_character) + 1, ord(second_character)):
        list_of_characters.append(chr(character))
    return list_of_characters

first_character = input()
second_character = input()
print(" ".join(single_string(first_character, second_character)))
