# Main part

name1 = input("Hello! What is your name?\n")
name2 = input("I know you have a best friend. What is their Name?\n")
print("I heard that you guys are stuck choosing a name for your band. I can help!\n")
city = input("What is your city?\n")
print(f"Your band name could be {city}" + " Rabbits " + str(len(name1) + len(name2)) + "\n\n")

# Exercise / Var values swapping

print(f"{name1} {name2}\n")
name1_temp = name1
name1 = name2
name2 = name1_temp
print(f"{name1} {name2}")
