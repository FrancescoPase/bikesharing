import csv
from datetime import datetime

for year in range(14,15):
    for month in range(1,9):

        filename = './data/20' + str(year) + '-0'+ str(month) + ' - Citi Bike trip data.csv'
        output = './parsed/data_customer' + str(year) + '0' + str(month) +'.csv'
        useful = [1, 0, 3, 7, 11, 13, 14]

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
                    date = datetime.strptime(changed[0], '%Y-%m-%d %H:%M:%S')
                    changed[0] = date.strftime('%s')
                    if (row[12] == 'Customer'):
                        continue
                    if (changed[5] == '\N'):
                        changed[5] = 0
                    changed.append(date.weekday())
                    writer.writerow(changed)
