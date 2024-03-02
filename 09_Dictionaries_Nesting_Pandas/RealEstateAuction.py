# Real Estate Auction

import pyarrow
import pandas as pd
from prettytable import PrettyTable
import tools

# All necessary variables
name = ""
bid = 0
bidders = []
highest_bid = 0
highest_bid_name = ""

# Setting up Lots data structure
lots = {
    "property": ["Apartment", "Townhouse", "Villa"],
    "location": ["Palmers Green, London, 413 Green Lanes, 4JD", "Laguna Park, Bang Tao, Thailand",
                 "Fethiye, Mugla, Turkey"],
    "bedrooms": [2, 3, 5],
    "area": [83, 170, 250],
    "starting_price": [600000, 250000, 500000]
}

all_bids = {
    "": ["Apartment", "Townhouse", "Villa"]
}

df_lots = pd.DataFrame(lots)

# Program starts
print("Welcome to Real Estate Auction!")
num_of_bidders = tools.to_int(input("\nHow many bidders are there? "))

if num_of_bidders == 0:
    exit()

for i in range(num_of_bidders):
    name = input("Enter bidder name: ")
    bidders.append(name)
    all_bids[bidders[i]] = []

# Starting auction
for index, row in df_lots.iterrows():
    print("\nProperty Type:", row['property'])
    print("Location:", row['location'])
    print("Bedrooms:", row['bedrooms'])
    print("Area:", row['area'], "sq.m.")
    print("Starting Price:", "${:,}".format(row['starting_price']))
    print("-" * 30)

    highest_bid = 0

    for i in range(num_of_bidders):
        bid = tools.to_int(input(f"{bidders[i]}'s bid: $"))

        if bid <= int(row['starting_price']):
            # If so, I warned you :)
            bid = tools.to_int(input("Bid above the starting price, otherwise you will lose: $"))

        all_bids[bidders[i]].append(bid)

df_bids = pd.DataFrame(all_bids)

# Final calculations
max_bids = df_bids.select_dtypes(include=[float, int]).max(axis=1).apply(lambda x: "${:,}".format(x))
winners_names = df_bids.select_dtypes(include=[float, int]).idxmax(axis=1)

table_bids = PrettyTable()
table_bids.field_names = df_bids.columns.tolist()

for index, row in df_bids.iterrows():
    table_bids.add_row(row.tolist())

table_bids.add_column("Max bid", max_bids)
table_bids.add_column("Winner", winners_names)

print("\n\nAuction results:")
print(table_bids)
