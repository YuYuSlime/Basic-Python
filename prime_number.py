a = input("aの値を入力: ")

# TODO
a = int(a)
i = 2
if a == 1:
    print("1です")
elif a < 0:
    print("負の数です")
else:
    while i * i <= a:
        if a % i == 0:
            print("合成数です")
            break
        i += 1
    else:
        print("素数です")
