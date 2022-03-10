import numpy as np


def get_bezier_coef(points):
    # given that len(points) == n+1 (from formula), n equals:
    n = len(points) - 1

    # build coefficients matrix
    C = 4 * np.identity(n)
    np.fill_diagonal(C[1:], 1)
    np.fill_diagonal(C[:, 1:], 1)
    C[0, 0] = 2
    C[n - 1, n - 1] = 7
    C[n - 1, n - 2] = 2

    # build points vector
    P = [2 * (2 * points[i] + points[i + 1]) for i in range(n)]
    P[0] = points[0] + 2 * points[1]
    P[n - 1] = 8 * points[n - 1] + points[n]

    # solve system, find a & b
    A = np.linalg.solve(C, P)
    B = [0] * n
    for i in range(n - 1):
        B[i] = 2 * points[i + 1] - A[i + 1]
    B[n - 1] = (A[n - 1] + points[n]) / 2

    return A, B


def get_cubic(p0, p1, p2, p3):
    return lambda t: np.power(1 - t, 3) * p0 + \
                     3 * np.power(1 - t, 2) * t * p1 + \
                     3 * (1 - t) * np.power(t, 2) * p2 + \
                     np.power(t, 3) * p3


def get_bezier_cubic(points):
    A, B = get_bezier_coef(points)
    return [get_cubic(points[i], A[i], B[i], points[i + 1]) for i in range(len(points) - 1)]


def bezier_approximation(points, n):
    curves = get_bezier_cubic(points)
    return np.array([fun(t) for fun in curves for t in np.linspace(0, 1, n)])
