text = input().split(" ")
text_str = ''.join(text)
characters = {}
for letter in text_str:
    if letter not in characters:
        characters[letter] = 0
    characters[letter] += 1
for key in characters.keys():
    print(f"{key} -> {characters[key]}")