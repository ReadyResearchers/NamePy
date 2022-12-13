# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon
    def __str__(self):
        return f'{self.name}, {self.lat}, {self.lon}'


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
import csv

cities = []

def cityreader(cities=[]):
# Implement the functionality to read from the 'cities.csv' file
# Ensure that the lat and lon valuse are all floats
# For each city record, create a new City instance and add it to the 
# `cities` list

    # opening the csv file
    data = list(csv.reader(open('cities.csv')))

    # pulling out city, lat, and lon
    city_lat_lon = [[x[0], float(x[3]), float(x[4])] for x in data[1:]]

    # appending cities to the cities list
    for i in range(len(city_lat_lon)):
        name = city_lat_lon[i][0]
        lat = city_lat_lon[i][1]
        lon = city_lat_lon[i][2]
        z = City(name, lat, lon)
        cities.append(z)

    return cities