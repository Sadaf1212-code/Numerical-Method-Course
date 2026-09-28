import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 + x - 1

def df(x):
    return 3*x**2 + 1

# Newton-Raphson
x = -0.7
n = 10

roots = []

for i in range(n):
    x = x - f(x) / df(x)
    roots.append(x)

    print(i + 1, x, f(x))

# Plot
x_values = np.linspace(-1, 1.2, 100)
y_values = f(x_values)

plt.plot(x_values, y_values)
plt.axhline(0)
plt.scatter(roots, [f(r) for r in roots])

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Newton-Raphson Method")
plt.grid()
plt.show()