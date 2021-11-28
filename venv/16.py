#2)Дан список со случайными числами. Создать новый список из всех элементов данного массива, которые кратны 5
from random import randint
# count = int(input("Введите количество элементов в списке\n"))
# for i in range(count):
#     player.append(int(input(f"Введите {i + 1} элемент\n")))
player = [randint(-100, 100) for x in range(20)]
print(player)
player = [i for i in player if i % 5 == 0]
print(player)