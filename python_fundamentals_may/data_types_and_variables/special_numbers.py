# def getSum(n):
#
#     sum = 0
#     for digit in str(n):
#         sum += int(digit)
#     return sum
#
# n = 12345
# print(getSum(n))


# integer = int(input())
# sum_digits = 0
# for number in range(1, integer + 1):
#     for digit in range(1, len(str(number)) + 1):
#         sum_digits += int(digit)
#     if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
#         print(f"{number} -> True")
#     else:
#         print(f"{number} -> False")

n = int(input())
for num in range(1, n+1):
    sum_of_digits = 0
    digits = num
    while digits > 0:
        sum_of_digits += digits % 10
        digits = int(digits/10)
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")



# A number is special when the sum of its digits is 5, 7, or 11.