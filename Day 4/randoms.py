import random

names_str = input("Names list: ")
names = names_str.split(", ")
random_integer = random.randint(0, len(names) - 1)
who_pays = names[random_integer]
print(who_pays)


