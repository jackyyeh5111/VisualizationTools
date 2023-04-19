""" 
    Draws a histogram using matplotlib and displays the percentage for each bar right above the bar
"""
import matplotlib.pyplot as plt
import numpy as np

# Generate some data
data = np.random.randn(1000)

# Create a histogram
n, bins, patches = plt.hist(data, bins=20)

# Calculate the percentage for each bar
percentages = 100 * n / n.sum()

# Set the text for each bar
for i in range(len(patches)):
    x = patches[i].get_x() + patches[i].get_width() / 2
    y = patches[i].get_height()
    plt.text(x, y, f'{percentages[i]:.1f}%', ha='center', va='bottom')

# Display the histogram
plt.show()
