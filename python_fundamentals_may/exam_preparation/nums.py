integers = [int(number) for number in input().split(" ")]
sum_integers = sum(integers)
average = sum_integers // int(str(len(integers)))
above_average = []
for number in integers:
    if number > average:
        above_average.append(number)
above_average = sorted(above_average, reverse=True)
above_average = above_average[0:5]
above_average_string = [str(number) for number in above_average]
if len(above_average_string) == 0:
    print("No")
else:
    print(' '.join(above_average_string))