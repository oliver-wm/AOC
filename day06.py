INPUT = """5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6"""

from collections import defaultdict


def to_list(input: str) -> list:
    return [int(cell) for cell in input.split()]


def to_pattern(l: list) -> str:
    return ''.join(str(l))


def find_MI(l: list):
    count = 0
    index = 0
    m = l[0]
    for i in l:
        if i > m:
            m = i
            index = count
        count += 1
    # assert max(l) == m
    # assert l.index(max(l)) == index
    return m, index


def distribute(max: int, index: int, l: list) -> list:
    l[index] = 0
    index += 1
    while max != 0:
        if index == len(l):
            index = 0
        l[index] += 1
        max -= 1
        index += 1
    return l


def cycles(blocks: list) -> int:
    count = 0
    patterns = {}
    patterns = defaultdict(lambda: 0, patterns)
    while to_pattern(blocks) not in patterns:
        # print(to_pattern(blocks))
        patterns[to_pattern(blocks)] += 1
        m, c = find_MI(blocks)
        blocks = distribute(m, c, blocks)
        count += 1

    patterns[to_pattern(blocks)] += 1
    # print(patterns)
    return count, patterns


count, patterns = cycles(to_list(INPUT))
l = max(patterns, key=patterns.get)
l = l[1:-1]
l = l.split(", ")
l = [int(c) for c in l]
num, pats = cycles(l)

print(num)

# assert cycles([0,2,7,0]) == 5
# assert cycles([2,4,1,2]) == 4
