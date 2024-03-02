# Bigger / Smaller Game
import random

ANIMALS = [
    "Ant", "Mouse", "Frog", "Sparrow", "Squirrel", "Rabbit", "Cat", "Raccoon", "Fox", "Coyote", "Sheep",
    "Pig", "Gorilla", "Horse", "Giraffe", "Hippopotamus"
]


def next_animal(exclude):
    animals_to_add = ANIMALS[:]
    animals_to_add.remove(exclude)
    return random.choice(animals_to_add)


score = 0
next_round = True
animals_pair = random.sample(ANIMALS, 2)

while next_round:
    guess = ""
    size_1 = ANIMALS.index(animals_pair[0])
    size_2 = ANIMALS.index(animals_pair[1])

    while guess not in ["0", "1"]:
        guess = input(f"Who is bigger: {animals_pair[0]} (0) or {animals_pair[1]} (1)? ")

    if animals_pair[int(guess)] == ANIMALS[max(size_1, size_2)]:
        score += 1
        print(f"Right! Score: {score}")
        animals_pair = [animals_pair[1], next_animal(animals_pair[1])]
    else:
        print(f"Wrong! Game over. Score: {score}")
        next_round = False


