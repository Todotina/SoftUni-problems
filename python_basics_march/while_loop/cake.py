width = int(input())
length = int(input())
size = width * length
pieces_left = size
command = input()
while command != "STOP":
    current_pieces = int(command)
    pieces_left = pieces_left - current_pieces
    if pieces_left <= 0:
        break
    command = input()

if pieces_left > 0:
    print(f"{abs(pieces_left)} pieces are left.")
else:
    print(f"No more cake left! You need {abs(pieces_left)} pieces more.")