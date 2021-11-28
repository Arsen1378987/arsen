# 3.	К кормушке прилетели воробьи, синицы, снегири и вороны. Мальчик посчитал количество птиц каждого вида. Напишите программу, которая запрашивает четыре числа – количество птиц каждого вида, а затем сообщает общее число птиц у кормушки, дописывая к числовому значению слово «птица» в правильной форме. Например, 33 птицы, 11 птиц, 21 птица.
# Входные данные: 4 натуральных  числа  А,В,C,D ( А,В,С,D  <=100).
# Выходные данные:  сумма переменных А,В,C,D и слово «птица» с согласованным окончанием.
# Пример:
# Ввод     2   5   8   1	Вывод     16 птиц
# Ввод    4   2   7   10  	Вывод     23 птицы
# Ввод    3   1   8   9	Вывод     21 птица
def getEndString(sum):
    result = ''
    if sum > 10 and sum < 20:
        result = 'птиц'
    else:
        number = sum % 10
        if number == 1:
            result = 'птица'
        elif number in [2, 3, 4]:
            result = 'птицы'
        else:
            result = 'птиц'
    return result

def getsumm(arr):
    result = 0
    for el in arr:
        result = result + el
    return result

# print(getEndString(1))
# print(getEndString(2))
# print(getEndString(3))
# print(getEndString(4))
# print(getEndString(5))

vod = [2, 5, 8, 1]
sum = getsumm(vod)
endstring = getEndString(sum)
print(f'{sum} {endstring}')


vod = [4, 2, 7, 10]
sum = getsumm(vod)
endstring = getEndString(sum)
print(f'{sum} {endstring}')


vod = [3, 1, 8, 9]
sum = getsumm(vod)
endstring = getEndString(sum)
print(f'{sum} {endstring}')


vod = [3, 1, 5, 2]
sum = getsumm(vod)
endstring = getEndString(sum)
print(f'{sum} {endstring}')



# vod2 = [4, 2, 7, 10]
# vod3 = [3, 1, 8, 9]
#
# endstring = 'птиц'
# endstring1 = 'птицы'
# endstring3 = 'птица'
#


# if   == 1:
#     print(f'{summ1} {endstring3}')
# if summ1%10 == [2, 3, 4]:
#     print(f'{summ1} {endstring1}')
# else:
#     print(f'{summ1} {endstring}')
# summ2 = vod2[0] + vod2[1] + vod2[2] + vod2[3]
# if summ2%10  == 1:
#     print(f'{summ2} {endstring3}')
# if summ2%10 == [2,3,4]:
#     print(f'{summ2} {endstring1}')
# if summ2%10 == [5, 6, 7, 8 , 9, 0]:
#     print(f'{summ2} {endstring}')
# summ3 = vod3[0] + vod3[1] + vod3[2] + vod3[3]
# if summ3%10  == 1:
#     print(f'{summ3} {endstring3}')
# if summ3%10 == [2, 3, 4]:
#     print(f'{summ3} {endstring1}')
# else:
#     print(f'{summ3} {endstring}')

