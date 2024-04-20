from fractions import Fraction

x = y = str()

while not x.isnumeric() or not y.isnumeric():
    try:
        x, y = input('Two numbers to sum separated with space (for ex.: 0 1): ').strip().split(' ')
    except ValueError:
        continue

print(f'Sum: {float(x) + float(y)}')

# Additional practice with Fractions

# n, m = input('\nTwo fractions to sum separated with space (for ex.: 1/2 3/4): ').strip().split(' ')
# f_sum = Fraction(n) + Fraction(m)
#
# if f_sum.numerator > f_sum.denominator:
#     whole_part = f_sum.numerator // f_sum.denominator
#     frac_part = str(f_sum.numerator % f_sum.denominator) + '/' + str(f_sum.denominator)
#     print(f'Sum: {f_sum}: {whole_part} and {frac_part}')
# else:
#     print(f'Sum: {f_sum}')
