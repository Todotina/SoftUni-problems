from collections import deque

string = input().split()
result = deque([])
for element in string:
    if element != "*" and element != "+" and element != "-" and element != "/":
        result.append(int(element))
    if element == "*":
        while len(result) > 1:
            product = result.popleft() * result.popleft()
            result.appendleft(product)
    elif element == "+":
        while len(result) > 1:
            product = result.popleft() + result.popleft()
            result.appendleft(product)
    elif element == "-":
        while len(result) > 1:
            product = result.popleft() - result.popleft()
            result.appendleft(product)
    elif element == "/":
        while len(result) > 1:
            product = result.popleft() // result.popleft()
            result.appendleft(product)

for element in result:
    print(element)
