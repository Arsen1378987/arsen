#1)Заполнить список из 10 элементов числами в интервале [-100,100] и переставить элементы так, чтобы все положительные элементы стояли в начала списка, а все отрицательные и нули*– в конце.
# Пример: исходный список: 20 -90 15 -34 10 0; результат: 20 15 10 -90 -34 0.
player = input().split()
player = [int(x) for x in player]
answer = []
for i in player:
    if i > 0:
        answer.append(i)
for i in player:
    if i <= 0:
        answer.append(i)

print(answer)
