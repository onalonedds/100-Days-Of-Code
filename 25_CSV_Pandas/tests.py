import pyarrow
import pandas as pd

data = pd.read_csv("weather_data.csv")  # data - DataFrame
# print(data["temp"].to_list())  # data["temp"] - Series
# print(data["temp"].mean(numeric_only=True))
#
# print(data.condition.to_list())
# print(data[data.day == "Monday"])
# print(data[data.temp == 14])

monday = data[data.day == "Monday"]
mtf = monday.temp[0] * 9/5 + 32
print(monday.temp.values)
