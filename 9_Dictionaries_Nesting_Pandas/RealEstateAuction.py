# PostgreSQL admin pass: q1w2e3r4

# Real Estate Auction

import pyarrow
import pandas as pd

# No error conversion to Int
def nect_int(user_input):
    if not user_input.isnumeric():
        return 0
    else:
        return int(user_input)

properties = [
    {
        "property": "Apartment",
        "description": {
            "location": "Palmers Green, London, 413 Green Lanes, 4JD",
            "bedrooms": 2,
            "area": 83,
            "starting_price": 600000
        }
    },
    {
        "property": "Townhouse",
        "description": {
            "location": "Laguna Park, Bang Tao, Thailand",
            "bedrooms": 3,
            "area": 170,
            "starting_price": 250000
        }
    },
    {
        "property": "Villa",
        "description": {
            "location": "Fethiye, Mugla, Turkey",
            "bedrooms": 5,
            "area": 250,
            "starting_price": 500000
        }
    }
]

df_lots = pd.DataFrame(properties)

name = ""
bid = 0
num_of_bidders = 0
bidders =  []
bidders_for_lot = {}
all_bids = {}
highest_bid = 0
highest_bid_name = ""

print("Welcome to Real Estate Auction!")

num_of_bidders = nect_int(input("How many bidders are there? "))

for i in range(num_of_bidders):
    name = input("Enter bidder name: ")
    bidders.append(name)
    bidders_for_lot[name] = 0

bidders_for_lot["Winner"] = ""

for index, row in df_lots.iterrows():
    all_bids[row['property']] = bidders_for_lot

df_bids = pd.DataFrame(all_bids)

for index, row in df_lots.iterrows():
    print("\nProperty Type:", row['property'])
    description = row['description']
    print("Location:", description['location'])
    print("Bedrooms:", description['bedrooms'])
    print("Area:", description['area'], "sq.m.")
    print("Starting Price:", "${:,}".format(description['starting_price']))
    print("-" * 30)

    highest_bid = 0

    for i in range(num_of_bidders):
        bid = nect_int(input(f"{bidders[i]}'s bid: $"))
        df_bids.loc[bidders[i], row['property']] = bid
        if bid > highest_bid:
            highest_bid = bid
            highest_bid_name = bidders[i]

    df_bids.loc["Winner", row['property']] = highest_bid_name

print(f"\nTable of lots, bidders, and winners:\n\n{df_bids}")






























