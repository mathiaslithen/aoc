#!/usr/bin/pypy3
# ruff: noqa: F401
import functools
import sys
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from math import lcm

from helpers import ALLD, DIAG, DIM, DRC, GFIND, INB, INTS, RC, ROT, VIS

sys.setrecursionlimit(10**5)
fn = sys.argv[1] if len(sys.argv) > 1 else '18.in'
with open(fn) as f:
    data = f.read().strip()
G = [INTS(line) for line in data.splitlines()]


def get_grid(S, data):
    g = [['.' for c in range(S+1)] for r in range(S+1)]
    for x, y in data:
        g[y][x] = '#'
    return g


def trav(data, S=70):
    end_pos = (S, S)
    G = get_grid(S, data)
    D = {}
    Q = deque([(0, (0, 0), [])])
    while Q:
        steps, pos, path = heappop(Q)
        r, c = pos
        if pos not in D or steps < D[pos]:
            D[pos] = steps
        else:
            continue
        if pos == end_pos:
            return steps
        for dr, dc in DRC():
            np = (rr, cc) = r + dr, c + dc
            if INB(G, rr, cc) and G[rr][cc] != '#' and np not in path:
                heappush(Q, (steps+1, np, path+[np]))


def f(data, part=1):
    if part == 1:
        return trav(data[:1024])
    mi, ma = 1024, len(data)
    while mi != ma:
        n = mi + ((ma - mi) // 2)
        if trav(data[:n]):
            mi = n+1
        else:
            ma = n
    return data[n]


print('A', f(G))
print('B', f(G, part=2))
