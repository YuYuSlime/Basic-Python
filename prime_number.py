# TODO
def prime(number: int):
    if not isinstance(number, int):
        raise ValueError("入力がint型ではありません。")
    if number <= 0:
        raise ValueError("入力が自然数ではありません。")
    if number == 1:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    else:
        return True


# examination
prime(10)
prime(2)
prime(61)
prime(1)
prime(0)
prime(3.14)
prime(-10)
prime("characters")
type(prime(10))
