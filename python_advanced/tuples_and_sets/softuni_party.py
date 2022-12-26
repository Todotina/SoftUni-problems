number_of_guests = int(input())
guest_list = set()
for code in range(number_of_guests):
    current_code = input()
    guest_list.add(current_code)
command = input()
while command != "END":
    guest_list.remove(command)
    command = input()
print(len(guest_list))
for code in sorted(guest_list):
    print(code)