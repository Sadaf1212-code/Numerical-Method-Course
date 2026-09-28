import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 + x - 1

a = 0
b = 1
old = 0
tol = 0.000001

print("Iter\tRoot\t\tError")

roots = []

for i in range(1, 100):
    root = (a + b) / 2
    error = abs(root - old)
    roots.append(root)

    print(i, "\t", round(root, 6), "\t", round(error, 6))

    if error < tol:
        break

    if f(a) * f(root) < 0:
        b = root
    else:
        a = root

    old = root

print("Final Root =", round(root, 6))

# Plot
x = np.linspace(0, 1, 100)
plt.plot(x, f(x))
plt.scatter(roots, [f(r) for r in roots])
plt.axhline(0)
plt.grid()
plt.show()