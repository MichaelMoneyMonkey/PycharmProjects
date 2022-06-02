# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#
#     temperatures = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#         print(row)
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

temp_list = data["temp"].to_list()
print(temp_list)

average_temp = sum(temp_list) / len(temp_list)

# optie 1 calc average
print(average_temp)
# optie 2 calc average with pandas
print(data["temp"].mean())
# get maximum number out of list with pandas
print(data["temp"].max())

# get data in Columns
print(data["condition"])
print(data.condition)

# get data in Row
# data.day = data["day"]
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp_fahrenheit = monday.temp * 9 / 5 + 32
print(monday_temp_fahrenheit)


# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")