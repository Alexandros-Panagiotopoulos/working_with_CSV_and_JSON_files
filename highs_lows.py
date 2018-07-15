import csv

from matplotlib import pyplot as plt
from datetime import datetime

# Get days and low-high temperatures from file
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, lows, highs = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        low = int(row [3])
        lows.append(low)
        high = int(row [1])
        highs.append(high)

print (highs)

# Plot data
fig = plt.figure(dpi=128, figsize= (10,6))
plt.plot(dates,highs, c='red', alpha = 0.5)
plt.plot(dates,lows, c='blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha=0.1)

# Format Plot
plt.title("Daily low-high temperatures, 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()