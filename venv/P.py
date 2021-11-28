#Выведите на экран числа 1, 2, 3, 4, ..., 20.
for i in range(1,21):
    if i == 20:
        print(i,end=".")
    else:
        print(i, end=", ")