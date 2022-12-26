expression = input()
stack = []
counter = 0
for index in range(len(expression)):
    character = expression[index]
    if character == "(":
        counter = index
        stack.append(counter)
    elif character == ")":
        counter = index
        print(expression[stack.pop():counter+1])
    else:
        counter = 0
