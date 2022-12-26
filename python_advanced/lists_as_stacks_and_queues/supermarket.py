from collections import deque

names = deque()
command = input()
while command != "End":
    if command != "Paid":
        names.append(command)
    else:
        while len(names):
            print(names.popleft())
    command = input()
print(f'{len(names)} people remaining.')

# command = input()
# names = []
# while command != "End":
#     if command != "Paid":
#         names.append(command)
#     else:
#         for element in names:
#             print(element)
#         names.clear()
#     command = input()
# print(f'{len(names)} people remaining.')

