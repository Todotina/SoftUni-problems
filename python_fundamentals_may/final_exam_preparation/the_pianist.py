number_of_pieces = int(input())
dict = {}
for i in range(number_of_pieces):
    current_piece = input().split("|")
    piece, composer, key = current_piece[0], current_piece[1], current_piece[2]
    if piece not in dict:
        dict[piece] = {}
        dict[piece]['composer'] = composer
        dict[piece]['key'] = key


command = input()
while command != "Stop":
    current_command = command.split("|")
    action = current_command[0]
    piece = current_command[1]
    if action == "Add":
        composer, key = current_command[2], current_command[3]
        if piece in dict:
            print(f"{piece} is already in the collection!")
        else:
            dict[piece] = {}
            dict[piece]['composer'] = composer
            dict[piece]['key'] = key
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif action == "Remove":
        if piece in dict:
            del dict[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif action == "ChangeKey":
        new_key = current_command[2]
        if piece in dict:
            dict[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()

for piece in dict:
    print(f"{piece} -> Composer: {dict[piece]['composer']}, Key: {dict[piece]['key']}")