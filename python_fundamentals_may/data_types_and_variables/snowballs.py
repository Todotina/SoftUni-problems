number_of_snowballs = int(input())
highest_value = 0
highest_weight = 0
highest_time = 0
highest_quality = 0
for ball in range(number_of_snowballs):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())
    current_value = int(current_weight / current_time) ** current_quality
    if current_value > highest_value:
        highest_value = current_value
        highest_weight = current_weight
        highest_time = current_time
        highest_quality = current_quality
print(f"{highest_weight} : {highest_time} = {highest_value} ({highest_quality})")