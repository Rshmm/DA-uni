import matplotlib.pyplot as plt

days = ["Mon", "Die", "Mitt", "Donn", "Frei", "Sams", "Sonn"]

Italy = [7,9,2,13,56,3,4]
Germany = [2,5,7,10,45,3,1]

plt.plot(days,Italy ,color='green', linestyle="dashed", label="Italy")
plt.plot(days,Germany ,color='red', label="Italy")


plt.grid()
plt.xlabel("Days")
plt.ylabel("Deaths")
plt.legend()
plt.savefig("covid-deaths")
plt.show()


