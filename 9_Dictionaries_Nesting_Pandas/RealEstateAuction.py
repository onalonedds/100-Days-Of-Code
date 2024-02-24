# PostgreSQL admin pass: q1w2e3r4

# To do: sell multiple items - Real Estate Auction.
import pyarrow
import pandas as pd

properties = [
    {
        "property": "Apartment",
        "description": {
            "location": "",
            "bedrooms": 1,
            "area": 50,
            "starting_price": 200000
        }
    },
    {
        "property": "House",
        "description": {
            "location": "",
            "bedrooms": 3,
            "area": 120,
            "starting_price": 1000000
        }
    }
]

df = pd.DataFrame(properties)
print(df)