start_with = int(input())
end_with = int(input())
new_string = ""
for character in range(start_with, end_with + 1):
    current_string = chr(character)
    new_string += current_string + " "
print(new_string)