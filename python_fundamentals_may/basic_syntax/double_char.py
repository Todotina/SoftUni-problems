command = input()
modified_string = ""
while command != "End":
    for letters in command:
        modified_string += letters * 2
    if command != "SoftUni":
        print(modified_string)
    modified_string = ""
    command = input()



    # text = "123abc"
    # result = ''
    # for letters in text:
    #     result += letters * 3
    #
    # print(result)