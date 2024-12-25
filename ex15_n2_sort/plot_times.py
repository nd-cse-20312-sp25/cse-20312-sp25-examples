#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = np.genfromtxt('sort_times.csv', delimiter=',', skip_header=1)

# Split the data into 4 arrays: time and 3 values
x  = data[:, 0]
y1 = data[:, 1]
y2 = data[:, 2]
y3 = data[:, 3]
y4 = data[:, 4]
y5 = data[:, 5]

# Plot all three lines
plt.plot(x, y1, label='selection', marker='o')
plt.plot(x, y2, label='insertion', marker='s')
plt.plot(x, y3, label='insertion improved', marker='s')
plt.plot(x, y4, label='bubble', marker='^') 
plt.plot(x, y5, label='bubble improved', marker='D') 

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
