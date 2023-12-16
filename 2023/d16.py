#!/usr/bin/python
import collections
import sys

fn = sys.argv[1] if len(sys.argv) > 1 else '16.in'
with open(fn) as f:
    data = f.read().strip()
lines = data.split('\n')
G = [[x for x in y] for y in lines]
R = len(G)
C = len(G[0])
dirs = {
    'down': (1, 0),
    'up': (-1, 0),
    'right': (0, 1),
    'left': (0, -1),
}


def vis(e):
    x = [['.' for _ in range(C)] for _ in range(R)]
    for row, col in e:
        x[row][col] = '#'
    for r in x:
        print(''.join(r))


def f(root):
    energized = set()
    seen = set()
    Q = collections.deque([root])
    while Q:
        (row, col), dir = Q.pop()
        dr, dc = dir
        rr = row + dr
        cc = col + dc
        new_pos = (rr, cc)
        if not (0 <= rr < R and 0 <= cc < C):
            continue
        energized.add(new_pos)
        new_dirs = []
        nxt = G[rr][cc]
        if (
            nxt == '.'
            or (not dr and nxt == '-')
            or (not dc and nxt == '|')
        ):
            new_dirs.append(dir)
        elif not dr and nxt == '|':
            new_dirs.append(dirs['up'])
            new_dirs.append(dirs['down'])
        elif not dc and nxt == '-':
            new_dirs.append(dirs['left'])
            new_dirs.append(dirs['right'])
        elif nxt == '/':
            if dr == 1:
                d = dirs['left']
            elif dr == -1:
                d = dirs['right']
            elif dc == 1:
                d = dirs['up']
            elif dc == -1:
                d = dirs['down']
            new_dirs.append(d)
        elif nxt == '\\':
            if dr == 1:
                d = dirs['right']
            elif dr == -1:
                d = dirs['left']
            elif dc == 1:
                d = dirs['down']
            elif dc == -1:
                d = dirs['up']
            new_dirs.append(d)
        else:
            assert False, '\t'.join(new_pos, nxt)
        for d in new_dirs:
            k = (new_pos, d)
            if k not in seen:
                Q.append(k)
                seen.add(k)
    return len(energized)


a = f(((0, -1), dirs['right']))
print(a)

start = []
for c in range(C):
    start.append(((-1, c), (1, 0)))
    start.append(((R, c), (-1, 0)))
for r in range(R):
    start.append(((r, -1), (0, 1)))
    start.append(((r, C), (0, -1)))
b = []
for x in start:
    b.append(f(x))
print(max(b))
