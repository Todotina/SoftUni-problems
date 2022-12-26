import re

pattern = r'@[a-zA-Z]{3,}@@[a-zA-Z]{3,}@|#[a-zA-Z]{3,}##[a-zA-Z]{3,}#'
string = input()
word_pairs = re.findall(pattern, string)
mirror_words = []
modified_words = []
if len(word_pairs) > 0:
    print(f"{len(word_pairs)} word pairs found!")
    for word in word_pairs:
        middle = int(len(word)/2)
        first_word = word[1:middle-1]
        second_word = word[middle+1:-1]
        if first_word == second_word[::-1]:
            mirror_words.append(word)
else:
    print("No word pairs found!")

if len(mirror_words) > 0:
    print("The mirror words are:")
    for mirror_word in mirror_words:
        if "#" in mirror_word:
            modified_word = mirror_word.replace("#", "")
            middle = int(len(modified_word)/2)
            modified_word = modified_word[:middle] + " <=> " + modified_word[middle:]
            modified_words.append(modified_word)
        elif "@" in mirror_word:
            modified_word = mirror_word.replace("@", "")
            middle = int(len(modified_word) / 2)
            modified_word = modified_word[:middle] + " <=> " + modified_word[middle:]
            modified_words.append(modified_word)
else:
    print("No mirror words!")

print(', '.join(modified_words))