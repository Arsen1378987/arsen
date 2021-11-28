t = int(input("температура"))
if t < -4:
    print("морозно")
if t < 0 and t >= 4:
    print("холодно")
if t >= 0  and t < 12:
    print("прохладно")
if t >= 12 and t < 27:
    print("тепло")
if t >= 27:
    print("жарко")

