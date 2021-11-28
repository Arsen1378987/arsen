#0 1 2 3 4 5
#0 1 2 3 4
#0 1 2 3
#0 1 2
#0 1
rows = 5
for row in range(rows, 0, - 1):
    for column in range(0, row + 1):
        print(column, end=' ')
    print('')



