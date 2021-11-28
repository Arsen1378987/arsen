#stack
#это структура данных предназначенная для хранения порядка
#последний пришел первый ушел
#опреции над стеками
#удаление последнего элемента,добавление элемента в конец стека


# 1. создать класс стек
# с двумя функцимя
# push и pop
'''
# класс стек описывает очередь
# в этом класс имеется атрибут stack для хранения информации об очереди,
# метод push для добавления элемента в конец очереди
# метод pop для удаления последнего элемнта очереди
# '''
# class Stack:
#     #self.stack - переменная в которой храним очередь,изначально очередь пустая
#     def __init__(self):
#         self.stack = []
#     #push() - функция которая добавляет переменную element в self.stack
#     #при вызове функции push() необходимо в параметре указать element который хотим добавить в конец очереди
#     def push(self,element):
#         self.stack.append(element)
#     '''
#     перед тем как удалить элемент мы проверяем наличие каких либо элементов в self.stack
#     если очередь пустая, то возвращаем None
#     '''
#     def pop(self):
#         if len(self.stack) > 0:
#             return self.stack.pop()
#         else:
#             return None
# object_stack = Stack()
# for i in range(0,10):
#     object_stack.push(i)
# print(object_stack.stack)
# for i in range(10):
#     print(f" {object_stack.pop()} итерация {i}")
# for i in range(5):
#     object_stack.push(i)
# element = 0
# its = 0
# print(object_stack.stack)
# while element != None:
#     element = object_stack.pop()
#     print(f" {element} итерация {its}")
#     its += 1


'''
Создать класс калькулятор
с функциями сложения вычитания умножения деления возведения во вторую степень
извлечения квадратного корня
Все эти операции применимы для двух или одной переменной 
'''

class Calculator:
    def __init__(self):
        self.stack = []

    c = 0
    p = 0
    u = 0
    o = 0
    g = 0

    def summ(self,x,y):
        c = x + y
        self.stack.append(c)

    def minus(self,x,y):
        p = x - y
        self.stack.append(p)

    def umnoz(self,x,y):
        u = x * y
        self.stack.append(u)

    def delen(self,x,y):
        o = x / y
        self.stack.append(o)

    def stepen(self,x):
        g = x * x
        self.stack.append(g)

object_calculator = Calculator()

object_calculator.summ(2,1)
print(object_calculator.stack[0])
object_calculator.summ(11,9)
print(object_calculator.stack[0])
object_calculator.summ(7,90)
print(object_calculator.stack[0])
object_calculator.minus(2,1)
print(object_calculator.stack[1])
object_calculator.umnoz(2,1)
print(object_calculator.stack[2])
object_calculator.delen(2,1)
print(object_calculator.stack[3])
object_calculator.stepen(2)
print(object_calculator.stack[4])