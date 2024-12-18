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


def get_grid(R, C, data):
    g = [['.' for c in range(C)] for r in range(R)]
    for x, y in data:
        g[y][x] = '#'
    return g


def trav(G, s=(0, 0), e=(70, 70)):
    walls = set(GFIND(G, '#'))
    Q = deque([(0, s, [])])
    P = []
    D = {}
    while Q:
        steps, pos, path = heappop(Q)
        r, c = pos
        if pos not in D or steps < D[pos]:
            D[pos] = steps
        else:
            continue
        if pos == e:
            P.append(steps)
        for dr, dc in DRC():
            np = (rr, cc) = r + dr, c + dc
            if INB(G, rr, cc) and np not in walls and np not in path:
                heappush(Q, (steps+1, np, path[:]+[np]))
    return P


def f(data, part=1):
    if part == 1:
        g = get_grid(71, 71, data[:1024])
        return min(trav(g))
    # for i in range(2500, 3000):
    for i in range(2851, 3000):
        g = get_grid(71, 71, data[:i])
        if not trav(g):
            return data[:i][-1]


print('A', f(G))
print('B', f(G, part=2))
