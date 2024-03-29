with open("text.txt", "a+") as file:
    file.write("\nNew text was added.")

with open("text.txt") as file:
    content = file.read()
    print(content)


