import numpy as np
import sympy as sp

def lagrange_interpolation(x_pts, y_pts):
    x = sp.Symbol('x')
    n = len(x_pts)
    P = 0
    
    for i in range(n):
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x - x_pts[j]) / (x_pts[i] - x_pts[j])
        P += y_pts[i] * L_i
        
    simplified_P = sp.simplify(P)
    
    print("Given Data Points:", list(zip(x_pts, y_pts)))
    print("-" * 45)
    print("Lagrange Interpolating Polynomial P(x):")
    print(simplified_P)
    
    return sp.Lambdify(x, simplified_P)

# Data points (-1,0), (2,1), (3,1), (5,2)
x_points = [-1, 2, 3, 5]
y_points = [0, 1, 1, 2]

poly = lagrange_interpolation(x_points, y_points)