import matplotlib.pyplot as plt

plt.scatter(2, 4)
plt.title("Square numbers", fontsize=14)
plt.xlabel("value", fontsize=14)
plt.ylabel("Square of value",fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
