doxod = int(input("твоя выручка"))
pasxod = int(input("твои расходы"))
cotrudniki = int(input("сколько у вас работает сотрудников"))
pribil = doxod - pasxod
penta = pribil/doxod   * 100
ih_pribil = pribil / cotrudniki
if pribil > 0:
   print(f"красавчик ты всего заработал {doxod} а с учётом трат {pribil} и твоя рента {penta}")
if pribil < 0:
   print(f"кароче ты полный лох и просрал {pribil}руб")
print(f"каждый сотрудник зарарботал {ih_pribil}руб")



