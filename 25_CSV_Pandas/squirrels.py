import pyarrow
import pandas as pd

data = pd.read_csv("Squirrel_Data.csv")
all_colors = data["Primary Fur Color"]

print(all_colors.value_counts())

# blacks = data[data["Primary Fur Color"] == "Black"]
# grays = data[data["Primary Fur Color"] == "Gray"]
# cinnamons = data[data["Primary Fur Color"] == "Cinnamon"]
#
# print(blacks.size)
# print(grays.size)
# print(cinnamons.size)
