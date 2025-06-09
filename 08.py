import matplotlib.pyplot as plt

days = ["Mon", "Die", "Mitt", "Donn", "Frei", "Sams", "Sonn"]

Italy = [7,9,2,13,56,3,4]
Germany = [2,5,7,10,45,3,1]

plt.bar(days,Italy ,color='green',  label="Italy",alpha= 0.5)
plt.bar(days,Germany ,color='red', label="Italy",alpha= 0.5)
plt.title("Covid deaths")

plt.grid()
plt.xlabel("Days")
plt.ylabel("Deaths")
plt.legend()
plt.savefig("covid-deaths")
plt.show()

