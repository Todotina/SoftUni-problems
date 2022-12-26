strings = input().split(" ")
first_string = strings[0]
second_string = strings[1]
first_string_codes = []
second_string_codes = []
total_sum = 0

for character in first_string:
    first_string_codes.append(ord(character))

for character in second_string:
    second_string_codes.append(ord(character))

if len(first_string_codes) > len(second_string_codes):
    for index in range(len(second_string_codes)):
        result = first_string_codes[index] * second_string_codes[index]
        total_sum += result
    for index in range(len(second_string_codes), len(first_string_codes)):
        total_sum += first_string_codes[index]
elif len(first_string_codes) < len(second_string_codes):
    for index in range(len(first_string_codes)):
        result = first_string_codes[index] * second_string_codes[index]
        total_sum += result
    for index in range(len(first_string_codes), len(second_string_codes)):
        total_sum += second_string_codes[index]
elif len(first_string_codes) == len(second_string_codes):
    for index in range(len(first_string_codes)):
        result = first_string_codes[index] * second_string_codes[index]
        total_sum += result

print(total_sum)
