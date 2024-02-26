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
    min_sum = 0
    max_sum = 0

    for card in card_set:
        try:
            int(card)
            min_sum += card
            max_sum += card
        except ValueError:
            if card == "A":
                min_sum += 1
                max_sum += 11
            else:
                min_sum += 10
                max_sum += 10

    return [min_sum, max_sum]

dealer_cards = [random.choice(cards), random.choice(cards)]
player_cards = [random.choice(cards), random.choice(cards)]

print_set(dealer_cards, True)

print(" ")

print_set(player_cards)

player_sum = card_sum(player_cards)
dealer_sum = card_sum(dealer_cards)

if 21 in player_sum:
    print("You win!")
    exit()
elif 21 in dealer_sum:
    print("Dealer wins!")
    exit()
elif 21 in player_sum and 21 in dealer_sum:
    print("Draw.")
    exit()

if "A" in player_cards:
    print(f"Player: {player_sum[0]}(A=1) or {player_sum[1]}(A=11)")
else:
    print(f"Player: {player_sum[0]}")

if player_sum[0] != 21 and player_sum[1] != 21:
    add_player_card = input("Wanna take one more card? y/n ")
    if add_player_card == "y":
        player_cards.append(random.choice(cards))
        player_sum = card_sum(player_cards)

while dealer_sum[1] < 19:
    dealer_cards.append(random.choice(cards))
    dealer_sum = card_sum(dealer_cards)

print_set(dealer_cards)
print(f"Dealer: {dealer_sum[1]}")

print_set(player_cards)
print(f"Player: {player_sum[1]}")

if 21 in player_sum:
     print("You win!")
elif 21 in dealer_sum:
     print("Dealer wins!")
elif player_sum[1] > dealer_sum[1]:
    print("You win!")
elif player_sum[1] == dealer_sum[1]:
    print("Draw.")
else:
    print("Dealer wins!")