a = int(input("пиши a"))
b = int(input("пиши b"))
i = 1
print(f"{i}-й день {a}")
while a < b:
   i = i + 1
   a = a / 10 + a
   print(f"{i}-й день {a}")
if a > b:
   print("пиши другое")