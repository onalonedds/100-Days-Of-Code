# Hangman Game

secret_word = "house"
attempts = 5
placeholder = ""

print(f"I thought of a {len(secret_word)} letter word.\nYou have {attempts} attempts to guess it.\nIf you know the word, type 'w[space][word].'")

for x in range(len(secret_word)):
    placeholder += "_"
print(placeholder)

def updated_placeholder(right_char, old_placeholder):
    new_placeholder = list(old_placeholder)
    for char in range(len(secret_word)):
        if right_char == secret_word[char]:
            new_placeholder[char] = right_char
    return ''.join(new_placeholder)

while attempts > 0:
    guess = input("Guess a letter or a word: ")

    if guess[0] == "w":
        if guess[2:] == secret_word:
            print("You win!")
            exit()
        else:
            attempts -= 1
            print(f"Wrong. You have {attempts} attempts left.")
    elif guess in secret_word:
        attempts -= 1
        placeholder = updated_placeholder(guess, placeholder)
        if attempts == 0:
            print(f"Right. You have 0 attempts left. Game over.")
            exit()
        else:
            print(f"Right. You have {attempts} attempts left.")
            print(placeholder)
    else:
        attempts -= 1
        if attempts == 0:
            print(f"Wrong. You have 0 attempts left. Game over.")
            exit()
        else:
            print(f"Wrong. You have {attempts} attempts left.")
            guess = input("Guess a letter or a word: ")