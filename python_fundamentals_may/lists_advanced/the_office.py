happiness = [int(number) for number in input().split(" ")]
factor = int(input())
happiness_factor = [number * factor for number in happiness]
total_count = len(happiness)
total_sum = sum(happiness_factor)
average_happiness = total_sum / total_count
happy_count = 0
for element in happiness_factor:
    if element >= average_happiness:
        happy_count += 1
if happy_count >= total_count // 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")

