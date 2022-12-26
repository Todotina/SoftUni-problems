from collections import deque

counter = 1
kids = deque(input().split())
number_of_tosses = int(input())
while len(kids) > 1:
    removed_kid = kids.popleft()
    if counter == number_of_tosses:
        print(f'Removed {removed_kid}')
        counter = 1
    else:
        counter += 1
        kids.append(removed_kid)
winner = kids.popleft()
print(f'Last is {winner}')
