summ = int(input("сколько вы хотите вложить?"))
year = int(input("на сколько лет вы готовы вложить ваши денньги?"))
while year > 0:
    year = year - 1
    summ = summ + summ / 10
    print(f"в  {year} год => {summ}руб")
    #print(f"через {years} лет ты получишь {vicnovok}")


