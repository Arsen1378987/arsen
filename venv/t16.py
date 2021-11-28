a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,4]
i = 0
while len(a) > i:
   if a[i] == 8:
      break  # break
   #print(i)
   if a[i] % 2 == 0:
       print(a[i])
   i = i + 1