import pandas
#
# data = pandas.read_csv("./weather_data.csv")
#
# monday_row=(data[data.day == "Monday"])
#
#
#
# temp_deg_cel = monday_row.temp[0]
#
# temp_deg_far =  (9/5 * temp_deg_cel) + 32
#
#
#
# print(temp_deg_far)


#create dataframe

data_dict = {
    "students" : ["Amy", "James", "shakir"],
    "scores" : [76,56,65]
}

data = pandas.DataFrame(data_dict)


print(data)