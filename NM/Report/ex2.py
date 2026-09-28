import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 2*x - 2

# False Position
a = 1
b = 2
n = 10

roots = []

for i in range(n):
    c = (a*f(b) - b*f(a)) / (f(b) - f(a))
    roots.append(c)

    print(i + 1, c, f(c))

    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

# Plot
x = np.linspace(1, 2, 100)
y = f(x)

plt.plot(x, y)
plt.axhline(0)
plt.scatter(roots, [f(r) for r in roots])

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("False Position Method")
plt.grid()
plt.show()