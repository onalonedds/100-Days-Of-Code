numbers = [12, -8, 4, 5, 9, 3]

l_min = l_max = numbers[0]

for number in numbers[1:]:
    # Option 1:
    # l_min = number if number < l_min else l_min
    # l_max = number if number > l_max else l_max

    # Option 2:
    l_min = number < l_min and number or l_min
    l_max = number > l_max and number or l_max

print(l_min, l_max)
