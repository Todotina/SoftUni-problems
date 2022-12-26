def operate(operator, *args):

    def add():
        return sum(args)

    def subtraction():
        tuple = (args)
        result = 0
        for ind in range(1, len(tuple) -1):
            result += (tuple[ind] - tuple[ind + 1])
        return result

    def multiplication():
        result = 1
        for el in args:
            result *= el
        return result

    def division():
        tuple = (args)
        result = 1
        for ind in range(1, len(tuple) -1):
            result += (tuple[ind] / tuple[ind + 1])
        return result

    if operator == "+":
        return add()
    elif operator == "-":
        return subtraction()
    elif operator == "*":
        return multiplication()
    elif operator == "/":
        return division()

print(operate("-", 1, 2, 3))
print(operate("/", 3, 4))