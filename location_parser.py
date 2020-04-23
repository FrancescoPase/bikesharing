import csv
from datetime import datetime

for year in range(13, 14):
    for month in range(7,10):

        filename = './data/20' + str(year) + '-0'+ str(month) + ' - Citi Bike trip data.csv'
        output = './parsed/local' + str(year) + '0' + str(month) +'.csv'
        useful = [3, 5, 6, 7, 9, 10]

        with open(filename, 'rb') as csvin:
            parser = csv.reader(csvin, delimiter=',', quotechar='"')
            with open(output, 'wb') as csvout:
                writer = csv.writer(csvout,delimiter=',')
                first = 0
                for row in parser:
                    if(first == 0):
                        first = 1
                        continue
                    changed = []
                    for index in useful:
                        changed.append(row[index])
                    writer.writerow(changed)
