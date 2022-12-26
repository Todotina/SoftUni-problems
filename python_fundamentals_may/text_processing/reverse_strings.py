command = input()
while command != "end":
    current_word = command
    reversed_word = current_word[::-1]
    print(f"{current_word} = {reversed_word}")

    command = input()
