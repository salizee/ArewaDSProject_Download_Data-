from datetime import datetime
import matplotlib.pyplot as plt
import csv

with open('path_to_your_csv_file.csv') as f:
	reader = csv.reader(f)
header_row = next(reader)

# Extract dates, and high and low temperatures.
dates, highs, lows = [], [], []
for row in reader:
	current_date = datetime.strptime(row[2], '%Y-%m-%d')
	high = int(row[4])
	low = int(row[5])
	dates.append(current_date)
	highs.append(high)
	lows.append(low)
	
# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')
# Format plot.
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)

