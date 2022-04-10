import math

i = 0
eps = 1e-10
x0 = input("x0: ")


def f(x):
    return math.pow(x,2)-4*(x)+4


def Df(x):
    return 2*(x)-4

print('i', "  x0", "  f(x0)", "  Df(x0)", "  x1", "  Dx")
while True:
    x1 = x0-f(x0)/Df(x0)
    Dx = math.fabs(x1-x0)
    print(i+1, "%.10f" % x0, "%.10f" % f(x0), "%.10f" % Df(x0), "%.10f" % x1, "%.10f" % Dx)
    i += 1
    x0 = x1
    if Dx < eps:
        break