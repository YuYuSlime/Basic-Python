import random
from math import pi


# TODO
# 自然数ではないものが入力されたときにNoneを返す
def euclid_gcd_calculator(a, b):
    if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
        return None
    while b:
        a, b = b, a % b
    return int(a)


# examination of Q.3
print(euclid_gcd_calculator(10, 20))
print(euclid_gcd_calculator(81, 91))
type(euclid_gcd_calculator(10, 20))
print(euclid_gcd_calculator(-10, 20))
print(euclid_gcd_calculator(10, "abcd"))


def coprime_bool(a, b):
    gcd_result = euclid_gcd_calculator(a, b)
    if gcd_result is None:
        return False
    return gcd_result == 1


# examination of Q.4
coprime_bool(10, 20)
coprime_bool(81, 91)
coprime_bool(10, "abcd")
type(coprime_bool(10, 20))
type(coprime_bool(10, "abcd"))


# extra


def generate_pairs(n):
    pairs = [(random.randint(1, 10**4), random.randint(1, 10**4)) for _ in range(n)]
    return pairs


pairs = generate_pairs(10**5)
coprime_count = sum(1 for a, b in pairs if coprime_bool(a, b))

print(coprime_count)
print(coprime_count / 10**5)
print(6 / (pi**2))
