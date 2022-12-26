number = int(input())
longest_intersection = []
for i in range(number):
    current_input = input().split("-")
    first = current_input[0].split(",")
    first_set = set()
    for item in range(int(first[0]), int(first[1]) + 1):
        first_set.add(item)
    second = current_input[1].split(",")
    second_set = set()
    for item in range(int(second[0]), int(second[1]) + 1):
        second_set.add(item)
    intersection = [element for element in first_set if element in second_set]
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection
print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")