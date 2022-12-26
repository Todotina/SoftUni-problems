from collections import deque

parentheses = deque(input())
while parentheses:
    left_part = parentheses.popleft()
    right_part = parentheses.pop()
    if (left_part == '{' and right_part == '}') or (left_part == '[' and right_part == ']') or (left_part == '(' and right_part == ')'):
        continue
    else:
        print("NO")
        break
if len(parentheses) == 0:
    print("YES")