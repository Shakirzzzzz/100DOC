# import csv
#
#
#
# with open("./weather_data.csv") as weather_file:
#    data  = csv.reader(weather_file)
#    tempratures = []
#
#    for i in data:
#       if i[1] != 'temp':
#          tempratures.append(i[1])
#
#
# print(tempratures)

#this was soo painful just to remove a column of data so we use  pandas library.

import pandas

data  = pandas.read_csv("./weather_data.csv")

print(data)

# temp_list = data["temp"].to_list()
#
# # sum = 0
# # length = len(temp_list)
# # for i in temp_list:
# #     sum += i
# # avg_temp = round(sum / length)
# # print(f"the average temprature is, {avg_temp}")
#
#
# # or
#
# print(data["temp"].mean())
#
# print(data["temp"].max())

# how to get data in a row

# print(data[data.day == "Friday" ])


max_temp = data["temp"].max()

print(data[data.temp == max_temp])
