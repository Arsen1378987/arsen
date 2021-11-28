#3) Заполнить список из 5 элементов числами. Найти сумму всех отрицательных элементов списка. Если отрицательных элементов в массиве нет, вывести сообщение «отрицательных элементов нет».
player = input().split()
player = [int(x) for x in player]
answer = 0
player = [i for i in player if i < 0]
for i in player:
    answer += i
if answer == 0:
    print("Нет отрицательных элементов")
else:
    print(answer)
