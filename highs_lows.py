import csv

from matplotlib import pyplot as plt
from datetime import datetime

# Get days and low-high temperatures from file
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, lows, highs = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            low = int(row [3])
            high = int(row [1])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


# Plot data
fig = plt.figure(dpi=128, figsize= (10,6))
plt.plot(dates,highs, c='red', alpha = 0.5)
plt.plot(dates,lows, c='blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha=0.1)

# Format Plot
plt.title("Daily low-high temperatures, 2014\nDeath Valley, CA", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
