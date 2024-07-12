# Working with csv files

import csv

with open("app01/extra/weather.csv", "r") as f:
    data = list(csv.reader(f))

def get_temp(station):
    for i in data[1:]: # removing csv headers
        if station == i[0]:
            temp = i[1]
        else:
            temp = "N.A."
    return temp

place = input("Enter station name: ").title().strip()
print(f"Temp in {place} is", get_temp(place))