message = input().split(" ")
final_message = []
first_letter = ''
code = ''
for word in message:
    for character in word:
        if character.isdigit():
            code += character
        else:
            break
    word = word.replace(code,'')
    first_letter = chr(int(code))
    if len(word) >= 2:
        word = first_letter + word[-1] + word[1:-1] + word[0]
    final_message.append(word)
    code = ''
print(' '.join(final_message))