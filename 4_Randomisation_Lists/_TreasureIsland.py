import random
import math

guess_area = int(input("Вы оказались на острове. Оглядитесь, как вы думаете, какова его примерная площадь в км?"))

sqrt_area = math.sqrt(guess_area)
a = round(sqrt_area)
b = round(guess_area / a)

if a * b == guess_area:
    print("Вы угадали!")
else:
    print(f"Вы почти угадали. Площадь острова {a * b}. Он простирается на {a} км на восток и на {b} км на север.")

treasure_map = []
line = []

for x in range(a):
    for y in range(b):
        line.append(y)
    treasure_map.append(line[:])
    line.clear()

tx = random.randint(0, a - 1)
ty = random.randint(0, b - 1)
print(treasure_map)

treasure_map[tx][ty] = "T"

print(treasure_map)

def check_map(user_guess):
    i = int(user_guess[0]) - 1
    j = int(user_guess[1]) - 1

    if treasure_map[i][j] == "T":
        print("Вы нашли сокровище!")
    else:
        user_guess = input("Здесь ничего нет. Куда дальше? (type N to quit): ")
        if user_guess.lower() != "n":
            check_map(user_guess)

guess_where = input("Вы находитесь на северо-западном краю острова. Сколько км вы пройдете на юг и сколько на восток? ")
check_map(guess_where)



