command = input()
sum = 0
while command != "NoMoreMoney":
    increase = float(command)
    if increase < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {increase:.2f}")
    sum += increase
    command = input()
print(f"Total: {sum:.2f}")

