import re


string = input()
searched_word = input()
pattern = fr'\b{searched_word}\b'
matches = re.findall(pattern, string, flags=re.IGNORECASE)
print(len(matches))