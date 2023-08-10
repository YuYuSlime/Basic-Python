a = input("aの値を入力: ")

# TODO
a = int(a)
i = 2
while i * i <= a:
    if a % i == 0:
        print("合成数")
        break
    i += 1
else:
    print("素数")
