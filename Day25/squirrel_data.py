import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250829.csv")
fur_data = data["Primary Fur Color"].to_list()

Cinnamon = 0
Gray = 0
Black = 0

for squirrel in fur_data:
    if squirrel == "Gray":
        Gray += 1
    elif squirrel == "Black":
        Black += 1
    elif squirrel == "Cinnamon":
        Cinnamon += 1


fur_data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [Gray, Cinnamon, Black]
}

data = pandas.DataFrame(fur_data_dict)
data.to_csv("new_fur_data.csv")
