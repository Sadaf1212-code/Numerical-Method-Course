import matplotlib.pyplot as plt  # type: ignore[reportMissingModuleSource]

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Straight Line")
plt.grid()
plt.show()