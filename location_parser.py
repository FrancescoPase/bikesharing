import csv
from datetime import datetime

for year in range(20, 21):
    for month in range(3, 4):

        filename = './data/JC-20' + str(year) + '0' + str(month) + \
                   '-citibike-tripdata.csv'
        output = './parsed/local_' + str(year) + '0' + str(month) + '.csv'
        useful = [3, 5, 6, 7, 9, 10]

        with open(filename, 'r') as csvin:
            parser = csv.reader(csvin, delimiter=',', quotechar='"')
            with open(output, 'w') as csvout:
                writer = csv.writer(csvout, delimiter=',')
                first = 0
                for row in parser:
                    if first == 0:
                        first = 1
                        continue
                    changed = []
                    for index in useful:
                        changed.append(row[index])
                    writer.writerow(changed)
