user_number = int(input('Enter a number n to find all prime numbers in range (1, n): '))


def is_prime(number):
    for divisor in range(2, int(user_number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


prime_numbers = list(filter(is_prime, range(1, user_number + 1)))

print(prime_numbers)
