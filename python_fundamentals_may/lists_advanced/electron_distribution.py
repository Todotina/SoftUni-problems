number_of_electrons = int(input())
filled_shells = []
remaining_electrons = number_of_electrons
for position in range(1, number_of_electrons):
    electrons_current_position = 2 * position ** 2
    if electrons_current_position <= remaining_electrons:
        filled_shells.append(electrons_current_position)
    else:
        filled_shells.append(remaining_electrons)
    remaining_electrons -= electrons_current_position
    if remaining_electrons <= 0:
        break
print(filled_shells)

# The maximum number of electrons in a shell can be 2n2, where n is the position of a shell (starting from 1).