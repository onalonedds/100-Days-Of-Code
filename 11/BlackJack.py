# Black Jack Game
import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

def print_card(card):
    if card == 10:
        print(f"[{card} ]")
    else:
        print(f"[{card}  ]")

def print_set(card_set, hide_first = False):
    to_print = card_set[:]
    if hide_first:
        to_print[0] = " "
    for card in to_print:
        print_card(card)

def card_sum(card_set):
    card_sum = 0
    for card in card_set:
        try:
            int(card)
            card_sum += card
        except ValueError:
            if card == "A":
                card_sum += 11
                if card_sum > 21:
                    card_sum -= 10
            else:
                card_sum += 10

    return card_sum

def check_black_jack():
    if player_sum == 21:
        print("You win!")
        exit()
    elif dealer_sum == 21:
        print("Dealer wins!")
        exit()
    elif player_sum == 21 and dealer_sum == 21:
        print("Draw.")
        exit()

dealer_cards = [random.choice(cards), random.choice(cards)]
player_cards = [random.choice(cards), random.choice(cards)]

print_set(dealer_cards, True)

print(" ")

print_set(player_cards)

player_sum = card_sum(player_cards)
dealer_sum = card_sum(dealer_cards)

check_black_jack()

print(f"Player: {player_sum}")

add_player_card = "y"

while add_player_card == "y":
    add_player_card = input("Wanna take one more card? y/n ")
    if add_player_card == "y":
        player_cards.append(random.choice(cards))
        player_sum = card_sum(player_cards)
        print_set(player_cards)
        print(f"Player: {player_sum}")

while dealer_sum < 17:
    dealer_cards.append(random.choice(cards))
    dealer_sum = card_sum(dealer_cards)

print_set(dealer_cards)
print(f"Dealer: {dealer_sum}")

print_set(player_cards)
print(f"Player: {player_sum}")

check_black_jack()

if player_sum > dealer_sum and player_sum < 21:
    print("You win!")
elif dealer_sum > player_sum and dealer_sum < 21:
    print("Dealer wins!")
elif player_sum > 21 and dealer_sum > 21:
    print("Draw.")
elif player_sum > 21 and dealer_sum < 21:
    print("Dealer wins!")
elif player_sum == dealer_sum:
    print("Draw.")