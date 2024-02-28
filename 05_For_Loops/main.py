# Student Heights
import random

student_heights = input().split()
number_of_students = len(student_heights)
max_height = 0

for n in range(0, number_of_students):
    student_heights[n] = int(student_heights[n])
    if student_heights[n] > max_height:
        max_height = student_heights[n]

total_height = sum(student_heights)
average_height = round(total_height / number_of_students)

print(f"{total_height}\n{number_of_students}\n{average_height}\n{max_height}")

# Sum of even numbers from range

x = int(input("Calculate sum of even numbers from 1 to "))
total = 0

for number in range(2, x+1, 2):
    total += number

print(total)

# Fizz Buzz Game

target = 20
for number in range(1, target + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Password generator

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = ''.join(password_list)

print(f"Your new password is {password}")