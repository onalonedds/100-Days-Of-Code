# Hangman Game

secret_word = "hangman"
attempts = 10
placeholder = "_" * len(secret_word)

print(f"I thought of a {len(secret_word)} letter word.\n"
      f"You have {attempts} attempts to guess it.\n"
      f"If you know the word, type 'w[space][word].'")

print(''.join(placeholder))

def updated_placeholder(right_char, old_placeholder):
    new_placeholder = list(old_placeholder)
    indices = [i for i, char in enumerate(list(secret_word)) if char == right_char]
    for index in indices:
        new_placeholder[index] = right_char
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
        if attempts == 0 and "_" in placeholder:
            print(f"Right! You have 0 attempts left. Game over.")
            exit()
        elif attempts == 0 and "_" not in placeholder:
            print(placeholder)
            print(f"Right! You win!")
            exit()
        elif "_" not in placeholder:
            print(placeholder)
            print(f"Right! You win with {attempts} attempts left!")
            exit()
        else:
            print(f"Right! You have {attempts} attempts left.")
            print(placeholder)
    else:
        attempts -= 1
        if attempts == 0:
            print(f"Wrong. You have 0 attempts left. Game over.")
            exit()
        else:
            print(f"Wrong. You have {attempts} attempts left.")