string = input()
modified_string = ''
strength = 0
for index in range(len(string)):
    if string[index] != ">" and strength > 0:
        strength -= 1
    elif string[index] == ">":
        strength += int(string[index+1])
        modified_string += string[index]
    else:
        modified_string += string[index]

print(modified_string)