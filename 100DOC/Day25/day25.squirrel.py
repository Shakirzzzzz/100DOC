import pandas

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_count_grey = len(data[data["Primary Fur Color"] == "Gray"])

print(fur_count_grey)   