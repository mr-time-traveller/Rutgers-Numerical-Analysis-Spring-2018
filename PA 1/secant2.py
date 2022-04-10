import math

x0 = input("x0: ")
x1 = input("x1: ")
eps = 1e-10
n = 0


def f(x):
    return math.pow(x,2)-4*(x)+4

print('n', " x0", "  x1", "    f(x0)", "  f(x1)", "  x2", " |Dx|")

while True:
    x2 = ((x0 * f(x1)) - (x1 * f(x0))) / (f(x1) - f(x0))
    Dx = math.fabs(x2 - x1)
    print(n+1, "%.10f" % x0, "%.10f" % x1, "%.10f" % f(x0), "%.10f" % f(x1), "%.10f" % x2, "%.10f" % Dx)
    x0 = x1
    x1 = x2
    n += 1
    if Dx < eps:
        break