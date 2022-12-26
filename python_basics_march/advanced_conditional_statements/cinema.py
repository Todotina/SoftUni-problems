projection_type = input()
rows = int(input())
columns = int(input())
number_of_seats = rows * columns
price = 0
if projection_type == "Premiere":
    price = 12.00
elif projection_type == "Normal":
    price = 7.50
elif projection_type == "Discount":
    price = 5.00
print(f"{number_of_seats * price:.2f} leva")
