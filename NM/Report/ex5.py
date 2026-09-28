import numpy as np
import matplotlib.pyplot as plt
# Lagrange interpolation
def lagrange(x, X, Y):
    result = 0

    for i in range(len(X)):
        term = Y[i]

        for j in range(len(X)):
            if i != j:
                term = term * (x - X[j]) / (X[i] - X[j])

        result += term

    return result
# Given points
X = [-1, 2, 3, 5]
Y = [0, 1, 1, 2]
# Interpolation at x = 4
x = 4
y = lagrange(x, X, Y)
print("Interpolated value at x =", x)
print("y =", y)
# Plot
x_values = np.linspace(-1, 5, 100)
y_values = [lagrange(x, X, Y) for x in x_values]
plt.plot(x_values, y_values, label="Lagrange Polynomial")
plt.scatter(X, Y, color="red", label="Given Points")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Lagrange Interpolation")
plt.grid()
plt.legend()
plt.show()