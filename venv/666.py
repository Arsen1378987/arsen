#Дан одномерный массив, состоящий из натуральных чисел. Выполнить сортировку данного массива по возрастанию суммы цифр чисел. Например, дан массив чисел [14, 30, 103].
#Например, дан массив чисел [14, 30, 103]. После сортировки он будет таким: [30, 103, 14], так как сумма цифр числа 30 составляет 3, числа 103 равна 4, числа 14 равна 5.
#ывести на экран исходный массив, отсортированный массив, а также для контроля сумму цифр каждого числа отсортированного массива.

a = [30, 103, 14]
i = 0
b = []
while i<len(a):
    print(a[i])

    b.append(a[i])
    i = i + 1
print(b)
