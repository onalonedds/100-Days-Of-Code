import math

def find_min_diff_pair(x):
    sqrt_x = math.sqrt(x)
    a = round(sqrt_x)
    b = round(x / a)
    pair = (a, b)
    return pair

print(find_min_diff_pair(163))
