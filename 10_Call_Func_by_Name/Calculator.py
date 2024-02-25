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

print("Operations available:")
for key in operations:
    print(f"{key} ({operations[key].__name__})")

while keep_working == "":
    if 'memory' in globals():
        x = input("\nEnter first operand or type 'm' to use prev result: ")
        if x == "m":
            x = memory
        else:
            x = tools.nect_int(x)
    else:
        x = tools.nect_int(input("\nEnter first operand: "))

    operation = input("Choose an operation (+ - * /): ")
    y = tools.nect_int(input("Enter second operand: "))

    if operation == "/" and y == 0:
        print(f"{x} {operation} {y} Error: division by zero.")
    else:
        action = operations[operation]
        result = action(x, y)
        memory = result
        print(f"{x} {operation} {y} = {result}\nMemory: {result}")
        keep_working = input("Press Enter to continue, any char to exit.")