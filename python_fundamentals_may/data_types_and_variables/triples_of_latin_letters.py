integer = int(input())

for first_letter in range(integer):
    for second_letter in range(integer):
        for third_letter in range(integer):
            print(f'{chr(97 + first_letter)}{chr(97 + second_letter)}{chr(97 + third_letter)}')
