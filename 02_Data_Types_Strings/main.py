# Main part

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_count = int(input("How many people to split the bill? "))

total_bill_tip = total_bill * (tip_percentage / 100 + 1)
bill_part = "${:,.2f}".format(total_bill_tip / people_count)

print(f"Each person should pay: {bill_part}")

# More about formatting number as currency https://stackabuse.com/format-number-as-currency-string-in-python/

# # Exercise / Two digits sum

two_digits_number = input("Enter any two digits number: ")
num_1 = int(two_digits_number[0])
num_2 = int(two_digits_number[1])
result = num_1 + num_2

print(f"The sum of these two digits is {result}")

# Exercise 2 / BMI calculator

height = float(input("What is your height in meters? "))
weight = float(input("What is your weight in kg's? "))

bmi = round(weight / height ** 2, 1)

print(f"Your BMI is {bmi}")

# Exercise 3 / Weeks in life left

age = int(input("How old are you? "))
weeks_per_year = 52
years_left = 80 - age
weeks_left = weeks_per_year * years_left

print(f"You have only {weeks_left} weeks left. Sorry...")
