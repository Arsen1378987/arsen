import json

class Car:

    #хранит переменные(состояния)
    def __init__(self):
        self.color = "red"
        self.motor = False
        self.doors = False
        self.light = False
        self.Times_of_day = True
        self.map = []
        self.home = [0,0]

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

    def cities(self):
        with open("Map.json") as infile:
            a = list(json.load(infile).keys())
            print(f" Список городов: {a} ")
            return a

    def choose_city(self,city):
        with open("Map.json") as infile:
            cities = json.load(infile)
        if cities.get(city) != None:
            self.map = cities[city]
            print("Карта города загружена")
            for i in range(len(self.map[0])):
                if self.map[0][i] == 1:
                    self.map[0][i] = "*"
                    self.home[0] = 0
                    self.home[1] = i
                    break
            return self.map
        else:
            print("Такого города не существует!")
            return None

    def right(self,steps):
        #Проверка на включение мотора
        if self.motor == True:
            #Проверка фар взависимоти от времени суток
            if (self.Times_of_day == False and self.light == True) or (self.Times_of_day == True):
                #Есть ли дорога в том месте куда мы хотит передвигаться
                if self.map[self.home[0]][self.home[1] + steps] == 1:
                    #Не выходим ли мы за границы карты
                    #********************************************----------------------------
                    if self.map[self.home[0]][self.home[1] + steps] < len(self.map[0]):
                        #Есть ли препятсвия на пути
                        '''
                        Равняется ли сумма эллементов от изначального местопложения и шагами ,которые мы хотим пройти
                        Элементы для суммирования берём с помощью среза self.home[1]+1:self.home[1]+1+steps
                        '''
                        _array_for_sum = self.map[self.home[0]][self.home[1]+1:self.home[1]+1+steps]
                        if sum(self.map[self.home[0]][self.home[1]+1:self.home[1]+1+steps]) == steps:
                            self.map[self.home[0]][self.home[1]] = 1
                            self.home[1] += steps
                            self.map[self.home[0]][self.home[1]] = "*"
                            for i in self.map:
                                print(*i)
                            print("right end")
                        else:
                            print("На пути препятствие!!!")

                    else:
                        print("ты выходишь за пределы карты")
                else:
                    print("Нет места")
            else:
                print("Включи фары")

        else:
            print("Включи мотор!")

    def down(self,steps):
        #Проверка на включение мотора
        if self.motor == True:
            #Проверка фар взависимоти от времени суток
            if (self.Times_of_day == False and self.light == True) or (self.Times_of_day == True):
                #Есть ли дорога в том месте куда мы хотит передвигаться
                if self.map[self.home[0] + steps][self.home[1]] == 1:
                    #Не выходим ли мы за границы карты
                    #********************************************----------------------------
                    if self.map[self.home[0]+ steps][self.home[1]] < len(self.map[0]):
                        summ = 0
                        #Сложение элемнтов от позиции звезды до новой позиции по строкам в переменную summ
                        for i in range(self.home[0]+1,self.home[0] + steps + 1):
                            summ += self.map[i][self.home[1]]
                        if summ == steps:
                            self.map[self.home[0]][self.home[1]] = 1
                            self.home[0] += steps
                            self.map[self.home[0]][self.home[1]] = "*"
                            for i in self.map:
                                print(*i)
                            print("down end")
                        else:
                            print("на пути препятствие")
                    else:
                        print("ты выходишь за пределы карты")
                else:
                    print(f"есть препятствие в точке куда хотим двигаться из точки {self.home[0]},{self.home[1]}")
            else:
                print("Включи фары")
        else:
            print("Включи мотор!")

    def up(self,steps):
        if self.motor == True:
            #Проверка фар взависимоти от времени суток
            if (self.Times_of_day == False and self.light == True) or (self.Times_of_day == True):
                #Есть ли дорога в том месте куда мы хотит передвигаться
                if self.map[self.home[0] - steps][self.home[1]] == 1:
                    #Не выходим ли мы за границы карты
                    if self.map[self.home[0] - steps][self.home[1]] < len(self.map[0]):
                        # Сложение элемнтов от позиции звезды до новой позиции по строкам в переменную summ
                        summka = 0
                        for i in range(self.home[0] - steps,self.home[0]):
                            summka = summka + self.map[i][self.home[1]]
                            print(self.map[i][self.home[1]])

                        if summka == steps:
                            self.map[self.home[0]][self.home[1]] = 1
                            self.home[0] = self.home[0] - steps
                            self.map[self.home[0]][self.home[1]] = "*"
                            for i in self.map:
                                print(*i)
                            print("down end")
                        else:
                            print("на пути препятствие")
                    else:
                        print(f"есть препятствие в точке куда хотим двигаться из точки {self.home[0]},{self.home[1]}")
                else:
                    print("Нет места")
            else:
                print("Включи фары")
        else:
            print("Включи мотор!")


    def left(self, steps):
        if self.motor == True:
            # Проверка фар взависимоти от времени суток
            if (self.Times_of_day == False and self.light == True) or (self.Times_of_day == True):
                # Есть ли дорога в том месте куда мы хотит передвигаться
                if self.map[self.home[0]][self.home[1] - steps] == 1:
                    # Не выходим ли мы за границы карты
                    if self.map[self.home[0]][self.home[1] - steps] < len(self.map[0]):
                        # Есть ли препятсвия на пути
                        '''
                        Равняется ли сумма эллементов от изначального местопложения и шагами ,
                        которые мы  хотим пройти
                        Элементы для суммирования берём с помощью среза self.home[1]-1:self.home[1]-1-steps
                        '''
                        _array_for_sum = self.map[self.home[0]][self.home[1] - steps:self.home[1]]
                        print(_array_for_sum)
                        if sum(_array_for_sum) == steps:
                            self.map[self.home[0]][self.home[1]] = 1
                            self.home[1] = self.home[1] - steps
                            self.map[self.home[0]][self.home[1]] = "*"
                            for i in self.map:
                                print(*i)
                            print("left end")
                        else:
                            print("На пути препятствие!!!")
                    else:
                        print("ты выходишь за пределы карты")
                else:
                    print("Нет места")
            else:
                print("Включи фары")
        else:
            print("Включи мотор!")
car = Car()
print(car.cities())
for i in car.choose_city("Moscow"):
    for y in i:
        if y == 1:
            print(f'\033[38;5;27m{y}\033[0;0m',end=" ")
        else:
            print(y,end=" ")
    print()
print(car.home)
car.open_close()
car.start()
car.down(1)
car.left(1)
car.down(2)
car.left(2)
car.right(2)
car.up(2)
car.right(2)
car.down(4)
car.Times_of_day = False
car.light_on()
car.left(3)
car.down(1)
