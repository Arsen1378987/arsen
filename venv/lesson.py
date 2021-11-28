#1.заполнение матрицы
a,b = list(map(int,input("Введите количество строк и столбцов: ").split()))
matrix = [list(map(int,input("Введите элементы строки ").split())) for i in range(a)]
#2.С помощью перебора найти самый большой элемент
max = matrix[0][0]
mini = matrix[0][0]
for i in matrix:
    for j in i:
        if max > j:
            max = j
        if mini < j:
            mini = j
#3. Все элементы заменены на разность между максимом и минимумом
for i in range(a):
    for j in range(b):
        matrix[i][j] = max - mini
for i in matrix:
    print(*i)

ащк ш шт фук for i ina