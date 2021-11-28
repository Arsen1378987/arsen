#Питон - это обьектно - ориентированый язык программирования
#класс - это описание обьекта
class Car:

    #хранит переменные(состояния)
    def __init__(self):
        self.color = "red"
        self.motor = False
        self.doors = False
        self.light = False
        self.Times_of_day = False
        self.map = []
        self.home = [0,0]

    #загрузка карты
    def enter_map(self,b,c):
        self.map = [list(map(int,input("Введите улицу: ").split())) for i in range(b)]
        for i in range(c):
            if self.map[0][i] == 1:
                self.map[0][i] = "*"
                self.home[1] = i
                break
        print("Карта загружена")

    #поехать вниз
    def down(self,step):
        if self.home[0] + step:
            self.map[self.home[0]][self.home[1]] = 1
        self.home[0] += step
        self.map[self.home[0]][self.home[1]] = "*"

    # поехать вверх
    def up(self,step):
        if self.home[0] - step:
            self.map[self.home[0]][self.home[1]] = 1
        self.home[0] -= step
        self.map[self.home[0]][self.home[1]] = "*"

    # поехать направо
    def right(self,step):
        if self.home[0] + step:
            self.map[self.home[1]][self.home[0]] = 1
        self.home[0] += step
        self.map[self.home[1]][self.home[0]] = "*"

    # поехать налево
    def right(self,step):
        if self.home[0] - step:
            self.map[self.home[1]][self.home[0]] = 1
        self.home[0] -= step
        self.map[self.home[1]][self.home[0]] = "*"

    #открытие и закрытие дверей
    def open_close(self):
        if self.doors == False:
            self.doors = True
            print("двери открыты")
        else:
            self.doors = False
            print("двери закрыты")

    #включение мотора
    def start(self):
        if self.doors == False:
            print("Двери закрыты")
        else:
            if self.motor == True:
                print("машина уже заведена")
            else:
                self.motor = True
                print("машина заведена")
    #выключение мотора
    def off(self):
        if self.motor == False:
            print("машина уже заглушена")
        else:
            self.motor = False
            print("машина заглушена")

    #включение света
    def light_on(self):
        if self.doors == False:
            print("Машина закрыта")
        else:
            if self.light == True:
                print("Свет уже включён")
            else:
                self.light = True
                print("Свет включён")

    #выключение света
    def light_off(self):
        if self.light == False:
            print("СВет уже выключен")
        else:
            self.light = False
            print("Свет выключен ")

'''
0 0 0 1
0 1 1 1
0 1 0 0
0 1 0 0
'''
#создание обьекта класса Car
car = Car()
a,b = list(map(int,input("Введите размеры города: ").split()))
car.enter_map(a,b)
print(car.map)
car.down(int(input("Введите количетсво шагов: ")))
for i in car.map:
    print(*i)

# 1. Машина заводилась, свет включался только после открытия дверей
#
#
# 1. Создать функцию, которая будет запрашивать карту города
#
# 2. Создать функции движения (вверх, вниз, вправо, влево)
