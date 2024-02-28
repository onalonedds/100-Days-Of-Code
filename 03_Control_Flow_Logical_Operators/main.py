# Even or odd number

number = int(input("Let's check if your number is even or odd: "))

if number % 2 == 0:
    print("It's even")
else:
    print("It's odd")

# Leap year check

year = int(input("Enter a year to check if it's a leap year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")

# Roller coaster

print("Welcome to the roller coaster!")

height = int(input("What is your height? "))
bill = 0

if height >= 120:
    print("You can ride!")
    age = int(input("What is your age? "))

    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a ride on us!")
    else:
        bill = 12
        print("Adult tickets are $14")

    wants_photo = input("Do you want a photo taken? Y or N: ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is {bill}")
else:
    print("Sorry, you have to grow taller.")

# Pizza order

bill = 0
size = input("What size pizza do you want? S, M, or L: ")

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("We don't have such pizzas :(")
    exit()

add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if add_pepperoni == "Y":
    bill += 2

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is {bill}")


# Love Calculator

print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is their name? ")
combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")