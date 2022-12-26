# string = input()
# new_string = ''
# for i in range(len(string)-1):
#     if string[i] != string[i+1]:
#         new_string += string[i]
# if string[-1] != new_string[-1]:
#     new_string += string[-1]
# print(new_string)

string = input()
new_string = string[0]
for index in range(len(string)):
    if new_string[-1] != string[index]:
        new_string += string[index]
print(new_string)