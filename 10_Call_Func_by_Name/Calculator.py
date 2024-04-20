# Calculator
import tools

x = 0
y = 0
keep_working = ""


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

memory = ""

print("Operations available:")
for key in operations:
    print(f"{key} ({operations[key].__name__})")

while keep_working == "":
    if memory:
        x = input("\nEnter first operand or type 'm' to use prev result: ")
        if x == "m":
            x = memory
        else:
            x = tools.to_float(x)
    else:
        x = tools.to_float(input("\nEnter first operand: "))

    operation = input("Choose an operation (+ - * /): ")
    y = tools.to_float(input("Enter second operand: "))

    if operation == "/" and y == 0:
        print(f"{x} {operation} {y} Error: division by zero.")
        memory = 0
    else:
        action = operations[operation]
        memory = action(x, y)
        print(f"{x} {operation} {y} = {memory}\nMemory: {memory}")
        keep_working = input("Press Enter to continue, any char to exit.")
