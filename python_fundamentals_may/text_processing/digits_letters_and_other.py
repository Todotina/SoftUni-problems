string = input()
digits = ''
letters = ''
characters = ''
for index in string:
    if index.isdigit():
        digits += index
    elif index.isupper() or index.islower():
        letters += index
    else:
        characters += index
print(digits)
print(letters)
print(characters)