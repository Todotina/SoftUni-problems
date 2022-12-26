def under_wealth(number, wealth):
    if number < min_wealth:
        return True


def over_wealth(number, wealth):
    if number > wealth:
        return True


def equal_wealth(number, wealth):
    if number == wealth:
        return True


population = [int(number) for number in input().split(', ')]
min_wealth = int(input())
distribution = []
negative_difference = 0
total_negative_difference = 0
positive_difference = 0
total_positive_difference = 0
under_wealth_list = []
over_wealth_list = []
for number in population:
    if over_wealth(number, min_wealth):
        positive_difference = number - min_wealth
        total_positive_difference += positive_difference
        over_wealth_list.append(number)
    elif under_wealth(number, min_wealth):
        negative_difference = min_wealth - number
        total_negative_difference += negative_difference
        under_wealth_list.append(number)
    elif equal_wealth(number, min_wealth):
        distribution.append(number)

if total_positive_difference > total_negative_difference:
    pass
else:
    print("No equal distribution possible")

