# 1. Parsing the CSV File Headers
# 2. These headers tell us what kind of information the data holds:
 
from pathlib import Path
import csv
path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

# Printing the Headers and Their Positions To make it easier to understand the file header data, let’s print each header and its position in the list:

reader = csv.reader(lines)
header_row = next(reader)
for index, column_header in enumerate(header_row):
 print(index, column_header)


# Extracting and Reading Data
reader = csv.reader(lines)
header_row = next(reader)
# Extract high temperatures.
highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)
print(highs)

#Plotting Data in a Temperature Chart
#To visualize the temperature data we have, we’ll first create a simple plot ofthe daily highs using Matplotlib, as shown here:

import matplotlib.pyplot as plt
path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()
# Plot the high temperatures.
import matplotlib.pyplot as plt

print(plt.style.available)

fig, ax = plt.subplots()
ax.plot(highs, color='red')
# Format plot.
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()


#The datetime Module
#Plotting Dates We can improve our plot by extracting dates for the daily high temperature readings, and using these dates on the x-axis:

from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt
path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and high temperatures.
dates, highs = [], []
for row in reader:
 current_date = datetime.strptime(row[2], '%Y-%m-%d')
 high = int(row[4])
 dates.append(current_date)
 highs.append(high)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')

# Format plot.
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()

#Plotting a Longer Timeframe
from pathlib import Path
import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

fig, ax = plt.subplots()
# Format plot.
ax.set_title("Daily High Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)

plt.show()


#Plotting a Second Data Series

