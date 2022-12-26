stack_clothes = input().split()
rack_capacity = int(input())
sum_clothes = 0
number_of_racks = 1
for item in range(len(stack_clothes)):
    current_item = int(stack_clothes.pop())
    sum_clothes += current_item
    if sum_clothes >= rack_capacity and len(stack_clothes) > 0:
        number_of_racks += 1
        sum_clothes = sum_clothes - rack_capacity
    if sum_clothes > 0 and len(stack_clothes) == 0:
        number_of_racks += 1
print(number_of_racks)