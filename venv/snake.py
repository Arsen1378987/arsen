import curses
from random import randint
# возможна ситуация, когда эти кординаты попадают на змейку. этого следует избежать, перегенерировав кординаты яблока, если они совпадают с одной из точек змейки.

def apple():
    global apple_x,apple_y,x,y
    apple_x = randint(1,maxx-1)
    apple_y = randint(1,maxy-1)
    #if apple_x and apple_y in zmeika:
    #     apple()
def main(sy):
    global maxx,maxy
    maxy,maxx=sy.getmaxyx()
    apple()
    x = 20
    y = 20
    zmeika = [(x,y)]
    while -1 > -2:
        k = sy.getch()
        sy.erase()
        sy.addstr(apple_y,apple_x,"apple")
        if k == ord("w"):
            y = y - 1
        if k == ord("s"):
            y = y + 1
        if k == ord("d"):
            x = x + 1
        if k == ord("a"):
            x = x - 1
        if x >= maxx:
            x = 0
        if y >= maxy:
            y = 0
        if x < 0:
            x = maxx-1
        if y < 0:
            y = maxy-1
        if apple_x == x and apple_y == y:
            apple()
        else:
            del zmeika[0]
        if (x,y) in zmeika:
            break
        zmeika.append((x,y))
        for i in range(0,len(zmeika),1):
            sy.addstr(zmeika[i][1],zmeika[i][0],"-")
curses.wrapper(main)
