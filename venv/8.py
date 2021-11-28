#1
#2 1
#3 2 1
#4 3 2 1
#5 4 3 2 1

rows = 5
for row in range(1, rows + 1):
    for column in range(row,0, - 1):
        print(column, end=' ')
    print('')
