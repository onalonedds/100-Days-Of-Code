from functools import reduce

user_number = int(input('Enter a number n to calculate the factorial n!: '))

factorial = reduce(lambda x, y: x * y, range(1, user_number+1))

print(f'The result is: {factorial}')
