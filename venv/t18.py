a = input("введи строку в которой мы будем искать число:")
b = input("введи само число")
i = 0
r = 0
while len(a) > i:
    if a[i] == b:
        r = r + 1
    i = i + 1
print(f"{r} раз")