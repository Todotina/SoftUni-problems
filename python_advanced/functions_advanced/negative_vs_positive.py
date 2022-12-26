def numbers(*args):
    args = [int(x) for x in input().split()]
    sum_positives = 0
    sum_negatives = 0
    for el in args:
        if el > 0:
            sum_positives += el
        else:
            sum_negatives += el
    print(sum_negatives)
    print(sum_positives)

    if sum_positives > abs(sum_negatives):
        return "The positives are stronger than the negatives"
    else:
        return "The negatives are stronger than the positives"

print(numbers())