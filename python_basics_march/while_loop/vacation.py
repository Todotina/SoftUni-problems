needed_money = float(input())
available_money = float(input())
total_days = 0
days_spending = 0
total_money = available_money
while needed_money > total_money:
    action = input()
    amount = float(input())
    total_days += 1
    if action == "save":
        total_money += amount
        days_spending = 0
    elif action == "spend":
        days_spending += 1
        total_money -= amount
        if amount > total_money:
            total_money = 0
        if days_spending == 5:
            print("You can't save the money.")
            print(total_days)
            break
if needed_money <= total_money:
    print(f"You saved the money for {total_days} days.")