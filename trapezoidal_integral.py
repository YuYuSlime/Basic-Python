from math import sin, pi

# --example--
a = 0
b = 0.5 * pi

print(sin(0))
print(sin(0.5 * pi))

h = (b - a) / 100
area = 0
area = 0.5 * (sin(a) + sin(b))

area = 0
for k in range(1, 101):
    left_end = sin(a + (k - 1) * h)
    right_end = sin(a + k * h)

    area += (left_end + right_end) * h / 2


print(area)
