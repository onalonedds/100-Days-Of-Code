# Auction

name = ""
bid = 0
more_bidders = "y"
all_bids = {}
highest_bid = 0
highest_bid_name = ""

print("Welcome to Auction!")

while more_bidders == "y":
    name = input("\nWhat is your name? ")
    bid = int(input("What is your bid? $"))
    all_bids[name] = bid
    more_bidders = input("Are there other bidders? y/n ")

for key, value in all_bids.items():
    if value > highest_bid:
        highest_bid = value
        highest_bid_name = key

print(f"\n{highest_bid_name} wins with a bid of ${highest_bid}.")