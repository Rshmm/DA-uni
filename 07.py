"""
This script visualizes COVID-19 death counts over a week for Italy and Germany using scatter plots.

Steps:
1. Defines days of the week as x-axis labels.
2. Specifies death counts for Italy and Germany.
3. Creates scatter plots for Italy (green) and Germany (red), with appropriate labels.
4. Adds grid lines, axis labels ("Days" and "Deaths"), and a legend.
5. Saves the plot as "covid-deaths.png".
6. Displays the plot.

This example demonstrates how to use matplotlib's scatter function to compare data points across categories.
"""

import matplotlib.pyplot as plt

days = ["Mon", "Die", "Mitt", "Donn", "Frei", "Sams", "Sonn"]

Italy = [7,9,2,13,56,3,4]
Germany = [2,5,7,10,45,3,1]

plt.scatter(days,Italy ,color='green',  label="Italy")
plt.scatter(days,Germany ,color='red', label="Germany")


plt.grid()
plt.xlabel("Days")
plt.ylabel("Deaths")
plt.legend()
plt.savefig("covid-deaths")
plt.show()

