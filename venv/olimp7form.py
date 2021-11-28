# 1.1.	Входной замок Лисы Алисы работает следующим образом: если введено натуральное число,
# которое меньше 100 или больше 999 – на дисплее устройства появляется надпись «FALSE»;
# если у введённого числа сумма цифр равна 13 – появляется надпись «ENTER» и можно войти; в остальных случаях появляется надпись «LOCK».
# Входные данные: натуральное число N ( ).
# Выходные данные: необходимо вывести надпись, которая должна быть на дисплее.
# Пример:
# Ввод     2	Вывод       FALSE
# Ввод     427	Вывод       ENTER
# Ввод    318	Вывод       LOCK

def test_task1(pasword):
  #  print(f"На входе {pasword}")
    if int(pasword) < 100 or int(pasword) > 999:
        print('FALSE')
    else:
        i = 0
        summa = 0
        while i < len(pasword):
            summa = summa + int(pasword[i]) + 1
            i = i + 1
        if summa == 13:
            print("ENTER")
        else:
            print("LOCK")

test1 = "2"
test_task1(test1)
# test2 = "427"
# test_task1(test2)
# test3 = "318"
# test_task1(test3)

paswo = input("Введи число")
test_task1(paswo)