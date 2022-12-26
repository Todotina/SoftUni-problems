from collections import deque
strings = deque(input().split())
colors = []
while strings:
    if len(strings) > 1:
        first_concatenation = strings[0] + strings[-1]
        second_concatenation = strings[-1] + strings[0]
        if first_concatenation == "red" or first_concatenation == "yellow" or first_concatenation == "blue" or first_concatenation == "orange" or first_concatenation == "purple" or first_concatenation == "green":
            strings.popleft()
            strings.pop()
            colors.append(first_concatenation)
        elif second_concatenation == "red" or second_concatenation == "yellow" or second_concatenation == "blue" or second_concatenation == "orange" or second_concatenation == "purple" or second_concatenation == "green":
            strings.popleft()
            strings.pop()
            colors.append(second_concatenation)
        else:
            new_first_string = strings[0][:-1]
            new_last_string = strings[-1][:-1]
            strings.popleft()
            strings.pop()
            middle = len(strings) // 2
            strings.insert(middle, new_first_string)
            strings.insert(middle, new_last_string)
    else:
        concatenation = strings[0]
        if concatenation == "red" or concatenation == "yellow" or concatenation == "blue" or concatenation == "orange" or concatenation == "purple" or concatenation == "green":
            strings.popleft()
            colors.append(concatenation)
        else:
            new_first_string = strings[0][:-1]
            if new_first_string == "":
                break
            strings.popleft()
            strings.insert(0, new_first_string)

if "orange" in colors and ("red" not in colors or "yellow" not in colors):
    colors.remove("orange")
if "purple" in colors and ("red" not in colors or "blue" not in colors):
    colors.remove("purple")
if "green" in colors and ("yellow" not in colors or "blue" not in colors):
    colors.remove("green")
print(colors)
# • orange = red + yellow
# • purple = red + blue
# • green = yellow + blue