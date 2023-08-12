from math import sin, pi

# --example--
a = 0
b = 0.5 * pi

n = 100
h = (b - a) / n

area = 0
for k in range(1, n + 1):
    left_end = sin(a + (k - 1) * h)
    right_end = sin(a + k * h)
    area += (left_end + right_end) * h / 2

print(area)
