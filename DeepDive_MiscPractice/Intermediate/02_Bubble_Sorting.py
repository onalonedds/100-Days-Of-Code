l = [5, 9, 3, 1, 45, 8, 16]
print(l)

for idx in range(len(l)):
    swapped = False
    for i in range(len(l) - idx - 1):
        if l[i] > l[i + 1]:
            l[i], l[i + 1] = l[i + 1], l[i]
            swapped = True
    if not swapped:
        break

print(f'Sorted: {l}')
