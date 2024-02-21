 # Guess the number game
import random

range_str = input("Define the range within which the random number is selected: ")
range_num = range_str.split()
number = random.randint(int(range_num[0]), int(range_num[1]))

#print(number)
def handle_user_input(user_input):
    if user_input == "":
        print("Good bye!")
        exit()
    elif not user_input.isnumeric():
        print("Your guess is -1. Next time enter a valid number.")
        return -1
    else:
        user_input = int(user_input)
        return user_input

guess = handle_user_input(input("Guess the number I selected, or press Enter to quit: "))
attempts = 0

while guess != number:
    if guess == -1:
        guess = handle_user_input(input("Try again, or press Enter to quit."))
        attempts += 1
    elif guess < number:
        guess = handle_user_input(input("Too low, try again, or press Enter to quit."))
        attempts += 1
    elif guess > number:
        guess = handle_user_input(input("Too high, try again, or press Enter to quit."))
        attempts += 1

print(f"Congratulations! You guessed the right number in {attempts} attempts.")