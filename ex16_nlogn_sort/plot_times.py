#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Load the data from the CSV file
# Assume the file has a header row, so we skip it (skiprows=1)
data = np.genfromtxt('sort_times.csv', delimiter=',', skip_header=1)

# Split the data into 4 arrays: time and 3 values
x  = data[:, 0]
y1 = data[:, 1]
y2 = data[:, 2]

# Plot all three lines
plt.plot(x, y1, label='merge', marker='*') 
plt.plot(x, y2, label='quick', marker='H') 

# Add labels and title
plt.xlabel('array size')
plt.ylabel('time (s)')
plt.title('Sort Times')

# Add a legend to distinguish each line
plt.legend()

# Save the figure
plt.savefig('sort_times.png')

# Display the plot
plt.show()
