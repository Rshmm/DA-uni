"""
This script visualizes COVID-19 death counts over a week for Italy and Germany using bar charts.

Steps performed:
1. Defines days of the week as x-axis labels.
2. Specifies death counts for Italy and Germany.
3. Plots two overlapping bar charts with semi-transparent colors (alpha=0.5) for comparison.
4. Adds a title, grid lines, axis labels ("Days" and "Deaths"), and a legend.
5. Saves the figure as "covid-deaths.png".
6. Displays the plot.

This example illustrates basic usage of matplotlib's bar charts and how to overlay them with transparency.
"""

import matplotlib.pyplot as plt

days = ["Mon", "Die", "Mitt", "Donn", "Frei", "Sams", "Sonn"]

Italy = [7,9,2,13,56,3,4]
Germany = [2,5,7,10,45,3,1]

plt.bar(days,Italy ,color='green',  label="Italy",alpha= 0.5)
plt.bar(days,Germany ,color='red', label="Germany",alpha= 0.5)
plt.title("Covid deaths")

plt.grid()
plt.xlabel("Days")
plt.ylabel("Deaths")
plt.legend()
plt.savefig("covid-deaths")
plt.show()

