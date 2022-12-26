capacity = float(input())
command = input()
available_free_space = capacity
suitcases_count = 0

while command != "End":
    current_suitcase_volume = float(command)
    if suitcases_count % 3 == 0:
        current_suitcase_volume *= 1.1
    available_free_space -= current_suitcase_volume
    if available_free_space < 0:
        print("No more space!")
        break
    suitcases_count += 1
    command = input()

if command == "End":
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {suitcases_count} suitcases loaded.")