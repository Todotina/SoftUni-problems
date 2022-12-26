stack = []
integer = int(input())
reversed_stack = []
for query in range(integer):
    current_query = input()
    if current_query == "2":
        if len(stack) >= 1:
            stack.pop()
        else:
            continue
    elif current_query == "3":
        print(max(stack))
    elif current_query == "4":
        print(min(stack))
    else:
        number = current_query.split()[1]
        stack.append(number)
while stack:
    reversed_stack.append(stack.pop())
print(', '.join(reversed_stack))