#!/usr/bin/python
import sys
from collections import deque

fn = sys.argv[1] if len(sys.argv) > 1 else '18.in'
with open(fn) as f:
    data = f.read().strip()
lines = data.split('\n')

dirs = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}
hexdirs = {
    '0': (0, 1),
    '1': (1, 0),
    '2': (0, -1),
    '3': (-1, 0),
}


def decode(s):
    s = s.strip('()#')
    d = s[-1]
    steps = int(s[:-1], base=16)
    return hexdirs[d], steps


def get_grid(lines, part=1):
    G = [(0, 0)]
    for line in lines:
        w = line.split()
        if part == 1:
            dr, dc = dirs[w[0]]
            steps = int(w[1])
        else:
            (dr, dc), steps = decode(w[2])
        row, col = G[-1]
        rr = row + (dr * steps)
        cc = col + (dc * steps)
        G.append((rr, cc))
    return G


def shift(grid):
    SG = []
    min_row = min(row for row, _ in grid)
    min_col = min(col for _, col in grid)
    for row, col in grid:
        if min_row < 0:
            row += abs(min_row)
        else:
            row -= abs(min_row)
        if min_col < 0:
            col += abs(min_col)
        else:
            col -= abs(min_col)
        SG.append((row, col))
    return SG


def get_rc(grid):
    R = max(row for row, _ in grid) + 1
    C = max(col for _, col in grid) + 1
    return R, C


def vis(grid):
    R, C = get_rc(grid)
    g = [['.' for _ in range(C)] for _ in range(R)]
    for r, c in grid:
        g[r][c] = '#'
    for x in g:
        print(''.join(x))


def get_start(grid):
    _x = [(row, col) for row, col in grid if col == 0]
    _y = [(row, col+1) for row, col in _x if (row, col+1) not in grid]
    return _y[0]


def bfs(grid):
    seen = set()
    S = get_start(grid)
    R, C = get_rc(grid)
    Q = deque([S])
    while Q:
        pos = Q.popleft()
        row, col = pos
        for dr, dc in (1, 0), (-1, 0), (0, 1), (0, -1):
            rr = row + dr
            cc = col + dc
            n = (rr, cc)
            if 0 <= rr < R and 0 <= cc < C:
                if n not in grid and n not in seen:
                    Q.append(n)
                    seen.add(n)
    print(len(seen) + len(grid))


def shoe(grid):
    # A = SUM [yi (xi-1 - xi+1)] / 2
    ret = 0
    lg = len(grid)
    for i in range(lg):
        ret += grid[i][1] * (grid[i-1][0] - grid[(i+1) % lg][0])
    return abs(ret) // 2


def boundry(grid):
    ret = 0
    for a, b in zip(grid, grid[1:]):
        ret += abs(a[0] - b[0])
        ret += abs(a[1] - b[1])
    return ret


def pick(grid):
    # A = i + b/2 - 1
    # => i = A - b/2 + 1
    A = shoe(grid)
    b = boundry(grid)
    i = A - b // 2 + 1
    return i + b


print('part1:', pick(get_grid(lines)))
print('part2:', pick(get_grid(lines, part=2)))
