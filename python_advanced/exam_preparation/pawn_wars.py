size = 8
board = []
for row in range(size, 0, -1):
    current_row = []
    for col in range(97, 97 + size):
        current_cell = chr(col) + str(row)
        current_row.append(current_cell)
    board.append(current_row)

white = ()
black = ()
for r in range(size):
    c_row = input().split()
    if "w" in c_row:
        c = c_row.index("w")
        white = (r, c)
    if "b" in c_row:
        c = c_row.index("b")
        black = (r, c)

w_row, w_col = white[0], white[1]
pos_white = board[w_row][w_col]
b_row, b_col = black[0], black[1]
pos_black = board[b_row][b_col]

for turn in range(14):
    if turn % 2 == 0:
        current_turn = "White"
        if board[w_row - 1][w_col - 1] == pos_black:
            print(f"Game over! {current_turn} win, capture on {pos_black}.")
            break
        w_row, w_col = w_row -1, w_col
        pos_white = board[w_row][w_col]
        if pos_white[1] == "8":
            print(f"Game over! {current_turn} pawn is promoted to a queen at {pos_white}.")
            break
    else:
        current_turn = "Black"
        if board[b_row + 1][b_col + 1] == pos_white:
            print(f"Game over! {current_turn} win, capture on {pos_white}.")
            break
        b_row, b_col = b_row + 1, b_col
        pos_black = board[b_row][b_col]
        if pos_black[1] == "1":
            print(f"Game over! {current_turn} pawn is promoted to a queen at {pos_black}.")
            break

