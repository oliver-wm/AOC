
from math import floor, sqrt


def find_point(num: int) -> int:
    if num == 1:
        return 0
    pow = 1
    num8s = 0
    gap = 0
    while num > pow * pow:
        num8s += 1
        pow += 2
        gap += 1

    spiral = []
    max = pow * pow
    for i in reversed(range(max - 8 * num8s + 1, max + 1)):
        spiral.append(i)

    r = pow - 2
    h = 2 * gap
    l = (2 * gap) - gap
    s = h
    d = 'D'
    spir = []
    for i in spiral:
        if i == num:
            return s
        # spir.append(s)
        if s == l:
            d = 'U'
        elif s == h:
            d = 'D'
        if d == 'D':
            s -= 1
        if d == 'U':
            s += 1


assert find_point(46) == 3
assert find_point(34) == 3
assert find_point(15) == 2
assert find_point(2) == 1
assert find_point(13) == 4
assert find_point(23) == 2
assert find_point(12) == 3
assert find_point(32) == 5
assert find_point(30) == 5
assert find_point(1024) == 31
assert find_point(29) == 4
assert find_point(1) == 0

print(find_point(361527))


def largest_val(num: int) -> int:

    spiral = [[int(0) for x in range(2 * num)] for y in range(2 * num)]
    x = y = num - 1
    print(x)
    print(y)

    spiral[x][y] = 1
    x, y = right(x, y)

    start = 1
    prevMove = 'U'
    while True:
        for i in range(0, 2):
            for j in range(0, start):
                x1, y1 = up(x, y)
                x2, y2 = down(x, y)
                x3, y3 = left(x, y)
                x4, y4 = right(x, y)
                x5, y5 = tleft(x, y)
                x6, y6 = tleft(x, y)
                x7, y7 = tright(x, y)
                x8, y8 = bleft(x, y)
                x9, y9 = bright(x, y)

                spiral[x][y] = spiral[x1][y1] + spiral[x2][y2] + spiral[x3][y3] \
                    + spiral[x4][y4] + spiral[x5][y5] + spiral[x6][y6] \
                    + spiral[x7][y7] + spiral[x8][y8] + spiral[x9][y9]
                print(spiral[x][y])
                print("\n")
                if spiral[x][y] > num:
                    return spiral[x][y]
                x, y = move(x, y, prevMove)
            x, y, prevMove = next_move(x, y, prevMove)
        start += 1
    print(spiral)


def move(x, y, prevMove):
    if prevMove == 'R':
        x, y = right(x, y)
    if prevMove == 'U':
        x, y = up(x, y)
    if prevMove == 'L':
        x, y = left(x, y)
    if prevMove == 'D':
        x, y = down(x, y)
    return x, y


def next_move(x, y, prevMove):
    if prevMove == 'R':
        x, y = right(x, y)
        prevMove = 'U'
    if prevMove == 'U':
        x, y = up(x, y)
        prevMove = 'L'
    if prevMove == 'L':
        x, y = left(x, y)
        prevMove = 'D'
    if prevMove == 'D':
        x, y = down(x, y)
        prevMove = 'R'
    return x, y, prevMove


def up(x, y):
    return x, y + 1


def down(x, y):
    return x, y - 1


def left(x, y):
    return x - 1, y


def right(x, y):
    return x + 1, y


def tleft(x, y):
    return x + 1, y + 1


def tright(x, y):
    return x - 1, y + 1


def bleft(x, y):
    return x - 1, y - 1


def bright(x, y):
    return x + 1, y - 1


largest_val(25)
