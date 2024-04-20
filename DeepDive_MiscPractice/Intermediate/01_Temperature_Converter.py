temp, units, convert_to = input('Enter temperature and specify current units and units '
                                'to convert to - F, C, or K. For example, 23 C K: ').lower().strip().split(' ')


def to_f(val, unit):
    if unit == 'c':
        return (val * 9 / 5) + 32
    elif unit == 'k':
        return (val - 273.15) * 9/5 + 32


def to_c(val, unit):
    if unit == 'f':
        return (val - 32) * 5/9
    elif unit == 'k':
        return val - 273.15


def to_k(val, unit):
    if unit == 'f':
        return (val - 32) * 5/9 + 273.15
    elif unit == 'c':
        return val + 273.15


match convert_to:
    case 'f':
        result = to_f(int(temp), units)
    case 'c':
        result = to_c(int(temp), units)
    case 'k':
        result = to_k(int(temp), units)

print(f'Result: {round(result, 2)} {convert_to.upper()}')

