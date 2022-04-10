import math

n = 0
eps = 1e-10
a = input("a: ")
b = input("b: ")


def f(x):
    return math.pow(x,2)-4*(x)+4


if f(a) * f(b) > 0:
    print "No root: The function values at the initial state should be opposite sign."
else:
    print("n", "  a", "  b", "    m", "    f(a)*f(m)", "|Dx/2|")
    while True:
        m = (a + b) / 2.0
        Dx = math.fabs((b - a) / 2.0)
        print(n+1, "%.10f" % a, "%.10f" % b, "%.10f" % m, "+" if f(a) * f(m) > 0 else "-", "%.10f" % Dx)
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
        n += 1
        if Dx < eps:
            break