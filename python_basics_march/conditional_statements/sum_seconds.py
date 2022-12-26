player1 = int(input())
player2 = int(input())
player3 = int(input())
result = player3 + player2 + player1
minutes = result // 60
seconds = result % 60
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")