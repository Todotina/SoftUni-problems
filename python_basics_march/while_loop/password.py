name = input()
password = input()
pass_confirm = input()
while pass_confirm != password:
    pass_confirm = input()
print(f"Welcome {name}!")
