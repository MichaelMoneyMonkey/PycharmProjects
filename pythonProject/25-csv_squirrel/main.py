import pandas

# get Primary Fur Color (3 possibilities)
# count them

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data.columns = data.columns.str.replace(' ', '_')
# print(data.Primary_Fur_Color)

gray_data = data.loc[data.Primary_Fur_Color == "Gray"]
gray = len(data.loc[data.Primary_Fur_Color == "Gray"])
print(gray)

cinnamon = len(data.loc[data.Primary_Fur_Color == "Cinnamon"])
black = len(data.loc[data.Primary_Fur_Color == "Black"])
print(cinnamon)
print(black)

data_dict = {
    "Fur color": ["gray", "cinnamon", "black"],
    "Count": [gray, cinnamon, black]
}
data = pandas.DataFrame(data_dict)
print(data)

# # create new table converted to csv
# data.to_csv("new_data.csv")













# make new data frame of result