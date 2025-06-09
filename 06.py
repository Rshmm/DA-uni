"""
This script plots the number of COVID-19 deaths over a week for Italy and Germany.

Steps:
1. Defines the days of the week as x-axis labels.
2. Provides death counts for Italy and Germany as separate lists.
3. Plots Italy's data with green dashed lines and Germany's data with red solid lines.
4. Adds grid lines, axis labels ('Days' and 'Deaths'), and a legend to distinguish the countries.
5. Saves the plot as 'covid-deaths.png'.
6. Displays the plot.

This example demonstrates basic line plotting with matplotlib and how to customize plot styles and labels.
"""

import matplotlib.pyplot as plt

days = ["Mon", "Die", "Mitt", "Donn", "Frei", "Sams", "Sonn"]

Italy = [7,9,2,13,56,3,4]
Germany = [2,5,7,10,45,3,1]

plt.plot(days,Italy ,color='green', linestyle="dashed", label="Italy")
plt.plot(days,Germany ,color='red', label="Germany")


plt.grid()
plt.xlabel("Days")
plt.ylabel("Deaths")
plt.legend()
plt.savefig("covid-deaths")
plt.show()


