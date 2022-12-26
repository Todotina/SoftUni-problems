command = input()

count_days = 1
reached_height = 5364
target_height = 8848

while command != "END":
    current_climbed_meters = int(input())
    reached_height += current_climbed_meters
    if command == "Yes":
        count_days += 1
    if reached_height >= target_height or count_days >= 5:
        break
    command = input()

if reached_height >= target_height:
    print(f"Goal reached for {count_days} days!")
else:
    print("Failed!")
    print(f"{reached_height}")