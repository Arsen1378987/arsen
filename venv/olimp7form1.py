# 2.	Даны три целых числа. Найти сумму двух наибольших из них.
# Входные данные: 3 целых  числа  А,В,C (-1000<= А,В,С  <=1000).
# Выходные данные:  сумма двух наибольших из них.
# Пример:
# Ввод      5  2  -13 Вывод    7
# Ввод     10  10  10 Вывод    20

#a = input("введи числа")
def bSort(array):
    # определяем длину массива
    length = len(array)
    #Внешний цикл, количество проходов N-1
    for i in range(length):
        # Внутренний цикл, N-i-1 проходов
        for j in range(0, length-i-1):
            #Меняем элементы местами, если число большt
            if array[j] < array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    print(array)

def test_task1(a,b,c):
    m = [a,b,c]
    for el in m:
        print(el)
    m.sort(reverse=True);
   # bSort(m)
    print(m[0] + m[1])

a = 5
b = 2
c =-13
test_task1(a,b,c)

a = 10
b = 10
c = 10
test_task1(a,b,c)