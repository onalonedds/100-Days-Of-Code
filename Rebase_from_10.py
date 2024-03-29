def rebase_from_10(n, b):
    if b < 2 or b > 36:
        raise ValueError('Base must be 2 <= b <= 36')

    sign = -1 if n < 0 else 1
    n *= sign

    if n == 0:
        return [0]

    digits = []

    while n > 0:
        n, m = divmod(n, b)
        digits.insert(0, m)

    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encoding = ''.join([digit_map[d] for d in digits])

    if sign == -1:
        encoding = '-' + encoding

    return encoding


print(rebase_from_10(5, 2))
