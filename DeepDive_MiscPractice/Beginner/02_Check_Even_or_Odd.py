def check(numb):
    return numb % 2 == 0 and 'Number is even.' or 'Number is odd.'


given_number = False

while not given_number:
    try:
        given_number = int(input('Number to check: '))
    except ValueError:
        continue

print(check(given_number))
