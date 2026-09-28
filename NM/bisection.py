def f(x):
    return x**3 + x - 1

a = 0
b = 1
tol = 0.000001

old_root = 0

print("Iteration\tRoot\t\tError")

for i in range(1, 100):

    root = (a + b) / 2

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