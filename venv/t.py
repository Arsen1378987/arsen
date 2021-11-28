#Пользователь вводит четыре числа. Найдите наибольшее четное число среди них. Если оно не существует, выведите фразу "not found"
x1 = int(input("введите число"))
x2 = int(input("введите число"))
x3 = int(input("введите число"))
x4 = int(input("введите число"))

if x1 % 2 != 0:     x1 = 0
if x2 % 2 != 0:     x2 = 0
if x3 % 2 != 0:     x3 = 0
if x4 % 2 != 0:     x4 = 0
if x1 > x2 and x1 > x3 and x1 > x4:
    print(x1)
if x2 > x1 and x2 > x3 and x2 > x4:
    print(x2)
if x3 > x1 and x3 > x2 and x3 > x4:
    print(x3)
if x4 > x1 and x4 > x3 and x4 > x2:
    print(x4)
if x1 == 0 and x2 == 0 and x3 == 0 and x4 == 0:
    print("not found")