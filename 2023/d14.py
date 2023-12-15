#!/usr/bin/python
import collections
import sys

fn = sys.argv[1] if len(sys.argv) > 1 else '14.in'
with open(fn) as f:
    data = f.read().strip()

rocks = set()
stops = set()

G = [[x for x in y] for y in data.split('\n')]
R = len(G)
C = len(G[0])

for row in range(R):
    for col in range(C):
        v = G[row][col]
        if v == 'O':
            rocks.add((row, col))
        elif v == '#':
            stops.add((row, col))


# n w s e
dirs = (-1, 0), (0, -1), (1, 0), (0, 1)


def vis(rocks):
    X = [['.' for _ in range(C)] for _ in range(R)]
    for r, c in stops:
        X[r][c] = '#'
    for r, c in rocks:
        X[r][c] = 'O'
    for x in X:
        print(''.join(x))


def score(rocks):
    ret = 0
    for row, col in rocks:
        ret += R - row
    return ret


def move(rocks, dir):
    s = set(rocks)
    dr, dc = dir
    for pos in s:
        row, col = pos
        rr, cc = row, col
        last_valid = pos
        while True:
            rr += dr
            cc += dc
            if (
                not (0 <= rr < R and 0 <= cc < C)
                or (rr, cc) in stops
            ):
                break
            if (rr, cc) not in rocks:
                last_valid = (rr, cc)
        if last_valid != pos:
            rocks.add(last_valid)
            rocks.remove(pos)


move(rocks, dirs[0])
print('part1', score(rocks))

CYCLE = 10**9
dd = collections.defaultdict(list)
i = 0
while i < CYCLE:
    i += 1
    for d in dirs:
        move(rocks, d)
    s = score(rocks)
    dd[s].append(i)
    if len(dd[s]) > 2:
        x = dd[s]
        loop = dd[s][-1] - dd[s][-2]
        i += (CYCLE-i)//loop * loop
print('part2', score(rocks))
