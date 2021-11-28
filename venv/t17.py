a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 96, 3]
i = 0
while len(a) > i:
    if a[i] == 89:
        break
    if a[i] % 2 == 0:
        print(f"{a[i]}")
    i = i + 1