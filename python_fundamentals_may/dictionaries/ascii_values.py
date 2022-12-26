list_of_characters = input().split(", ")
dict_values = {character: ord(character) for character in list_of_characters}
print(dict_values)