from math import sin, pi, sqrt, exp


# TODO
def func2(x):
    return 4 / (1 + x**2)


def func3(x):
    return sqrt(pi) * exp(-(x**2))


def trapezoidal_integral(f, a=0, b=1, n=100):
    h = (b - a) / n
    area = 0
    for k in range(n):
        left_end = f(a + k * h)
        right_end = f(a + (k + 1) * h)
        area += (left_end + right_end) * h / 2
    return area


print(trapezoidal_integral(sin, 0, pi / 2, 50))
print(trapezoidal_integral(func2, 0, 1, 100))
print(trapezoidal_integral(func3, -100, 100, 1000))
