import re

emoji_pattern = r'(\:{2}[A-Z][a-z][a-z]+\:{2})|(\*{2}[A-Z][a-z][a-z]+\*{2})'
# r'[0-9]|(\:{2}[A-Z][a-z]{2,}\:{2})|(\*{2}[A-Z][a-z]{2,}\*{2})'
numbers_pattern = r'\d'
string = input()
emoji_matches = re.findall(emoji_pattern, string)
numbers_matches = re.findall(numbers_pattern, string)

cool_emojis = []
cool_threshold = 1
for number in numbers_matches:
    cool_threshold *= int(number)
for emoji in emoji_matches:
    sum_characters = 0
    if len(emoji[0]) > len(emoji[1]):
        for character in emoji[0][2:-2]:
            sum_characters += int(ord(character))
    elif len(emoji[0]) < len(emoji[1]):
        for character in emoji[1][2:-2]:
            sum_characters += int(ord(character))
    if sum_characters > cool_threshold:
        cool_emojis.append(emoji)
print(f"Cool threshold: {cool_threshold}")
print(f"{len(emoji_matches)} emojis found in the text. The cool ones are:")
for cool_emoji in cool_emojis:
    print(''.join(cool_emoji))