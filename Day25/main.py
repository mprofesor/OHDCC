#with open("weather_data.csv", mode="r") as data_file:
#    data = data_file.readlines()
#    print(data)
#
#import csv

#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperature = []
#    for row in data:
#        if row[1] != "temp":
#            temperature.append(int(row[1]))
#        #print(row)
#
#print(temperature)


import pandas 

data = pandas.read_csv("weather_data.csv")
#print(type(data))

#print(type(data["temp"]))


sum_temp = 0
temp_list = data["temp"].to_list()
for day_temp in temp_list:
    sum_temp += day_temp

avg_temp = sum_temp / len(temp_list)

#print(avg_temp)

#print(data["temp"].mean())

#print(data["temp"].max())

#print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(f"{monday.temp[0]}C = {monday.temp[0] * (9/5) + 32}F")


# Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")