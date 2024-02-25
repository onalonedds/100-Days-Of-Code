# Calculator
import tools

x = 0
y = 0
keep_working = ""

def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

while keep_working == "":
    x = tools.nect_int(input("\nEnter first operand: "))
    operation = input("Choose operation (+ - * /): ")
    y = tools.nect_int(input("Enter second operand: "))

    if operation == "/" and y == 0:
        print(f"{x} {operation} {y} Error: division by zero.")
    else:
        action = operations[operation]
        result = action(x, y)
        print(f"{x} {operation} {y} = {result}")
        keep_working = input("Press Enter to continue, any char to exit.")