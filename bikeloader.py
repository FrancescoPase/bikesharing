import numpy as np
import csv
import geopy.distance


class BikeLoader:
    
    bikes = {}  # structure with bike sharing data
    locations = {}  # dictionary with stop IDs and location
    times = []

    def __init__(self, filename):
        # load data
        bike_file = open(filename, 'rt')
        parser = csv.reader(bike_file, delimiter=',', quotechar='"')
        for row in parser:
            if float(row[1]) not in self.times:
                self.times.append(float(row[1]))
            if row[0] not in self.bikes:
                self.bikes[row[0]] = {}
            self.bikes[row[0]][float(row[1])] = row[4:6]
            self.locations[row[0]] = row[2:4]
            
    def get_stations(self):
        return list(self.bikes.keys())
        
    def get_times(self):
        return self.times
        
    def get_location(self, station):
        return self.locations[station]
        
    def get_demand(self, station, t):
        value = self.bikes[station].get(float(t))
        if (value):
            return value
        else:
            return [0, 0]
            
    def get_nearby(self, station, number, t):
        coord = self.locations[station]
        nearby = []
        # get closest stations
        closest = sorted(list(self.locations.items()),
                         key=lambda x: geopy.distance.vincenty(
                             coord, x[1]).km)
        
        for i in range(1, number + 1):
            dock = closest[i][0]
            nearby = [dock]
            nearby.extend(self.get_demand(dock, t))
            
        return nearby
