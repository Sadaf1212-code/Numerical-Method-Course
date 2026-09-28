try:
    import matplotlib.pyplot as plt  # type: ignore[import-not-found]
except ModuleNotFoundError:
    plt = None


def f(x):
    return x**3 + x - 1

a = 0
b = 1
tol = 0.000001

old_root = 0

print("Iteration\tRoot\t\tError")

for i in range(1, 100):

    root = (a*f(b) - b*f(a)) / (f(b) - f(a))
    error = abs(root - old_root)

    print(i, "\t\t", round(root, 6), "\t", round(error, 6))

    if error < tol:
        break

    if f(a) * f(root) < 0:
        b = root
    else:
        a = root

    old_root = root

print("\nFinal Root =", round(root, 6))

# Plot (only if matplotlib is installed)
if plt is not None:
    x = [i/10 for i in range(0, 11)]
    y = [f(i) for i in x]

    plt.plot(x, y)
    plt.axhline(0)
    plt.axvline(root)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("False Position Method")
    plt.grid()
    plt.show()
else:
    print("matplotlib is not installed; skipping plot.")