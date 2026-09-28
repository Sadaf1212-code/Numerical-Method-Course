import math

def f(x):
    return math.sin(x) - 0.5

a = 0
b = 1

for i in range(20):

    c = (a + b) / 2

    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

print("Root =", c)