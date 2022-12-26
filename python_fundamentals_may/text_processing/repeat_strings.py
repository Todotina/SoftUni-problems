string = input().split(" ")
repeated_strings = []
for word in string:
    times_to_repeat = int(len(word))
    new_string = word * times_to_repeat
    repeated_strings.append(new_string)
print(''.join(repeated_strings))