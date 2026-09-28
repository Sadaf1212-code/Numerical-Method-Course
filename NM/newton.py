def f(x):
    return x**3 + x - 1

def df(x):
    return 3*x**2 + 1

root = 0.5
tol = 0.000001

print("Iteration\tRoot\t\tError")

for i in range(1, 100):

    new_root = root - f(root) / df(root)

    error = abs(new_root - root)

    print(i, "\t\t", round(new_root, 6), "\t", round(error, 6))

    if error < tol:
        root = new_root
        break

    root = new_root

print("\nFinal Root =", round(root, 6))

# Plot (optional; install matplotlib to enable it)
try:
    import importlib
    plt = importlib.import_module("matplotlib.pyplot")

    x = [i / 10 for i in range(0, 11)]
    y = [f(i) for i in x]

    plt.plot(x, y)
    plt.axhline(0)
    plt.axvline(root)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Newton-Raphson Method")
    plt.grid()
    plt.show()
except ImportError:
    print("Plot skipped: install matplotlib to display the graph.")
