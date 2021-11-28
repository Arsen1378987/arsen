rows = 5

for row in range(1, rows + 1):
    for column in range(1, rows - row + 2):
        num = rows - row + 1
        print(num, end=' ')
    print('')