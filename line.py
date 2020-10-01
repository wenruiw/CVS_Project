import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv","r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)



highs = []
dates = []
lows  = []

for row in csv_file:
    try:
        high=(int(row[5]))
        low=(int(row[6]))
        current_date = datetime.strptime(row[2],'%Y-%m-%d')

    except ValueError:
        print(f"Missing date for {current_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)


open_file2 = open("sitka_weather_2018_simple.csv","r")

csv_file2 = csv.reader(open_file2, delimiter=",")

header_row2 = next(csv_file2)



highs2 = []
dates2 = []
lows2  = []

for row in csv_file2:
    try:
        high2=(int(row[5]))
        low2=(int(row[6]))
        current_date2 = datetime.strptime(row[2],'%Y-%m-%d')
    except ValueError:
        print(f"Missing date for {current_date}")
    else:
        highs2.append(high2)
        lows2.append(low2)
        dates2.append(current_date2)

import matplotlib.pyplot as plt



fig, ax = plt.subplots(2,sharex='col')
fig.suptitle('Temperature Comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US',fontsize=10)

 
ax[0].plot(dates, highs,c='red',alpha=0.5)
ax[0].plot(dates, lows,c='blue',alpha=0.5)
ax[0].fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) 
ax[0].set_title('Death Valley,CA US',fontsize=10)





ax[1].plot(dates2, highs2,c='red',alpha=0.1)
ax[1].plot(dates2, lows2,c='blue',alpha=0.1)
ax[1].fill_between(dates2, highs2, lows2, facecolor='blue', alpha=0.1)
ax[1].set_title('SITKA AIRPORT,AK US')



plt.show()





