# "multiply", "divide", "add", "subtract"
action = input()
first_number = int(input())
second_number = int(input())

def mat_operation(first_number, second_number, action):
    if action == "multiply":
        return first_number * second_number
    elif action == "divide":
        return first_number / second_number
    elif action == "add":
        return first_number + second_number
    elif action == "subtract":
        return first_number - second_number
print(int(mat_operation(first_number, second_number, action)))