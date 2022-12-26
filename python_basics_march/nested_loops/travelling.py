destination = input()

while destination != "End":
    budget = float(input())
    saved_money = 0
    while budget > saved_money:
        current_sum = float(input())
        saved_money += current_sum
    print(f"Going to {destination}!")
    destination = input()
