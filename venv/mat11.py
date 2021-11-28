beard = int(input("сколько букв в алфавите?"))
i = 1
if beard == 33:
   print(f"ответ верный с {i} попытки")
else:
   i = i + 1
   beard = int(input("сколько букв в алфавите?"))
   if beard == 33:
      print(f"ответ верный с {i} попытки")
   else:
      i = i + 1
      beard = int(input("сколько букв в алфавите?"))
      if beard == 33:
         print(f"ответ верный с {i} попытки")
      else:
         print("попытки исчерпаны")

