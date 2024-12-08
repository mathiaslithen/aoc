#!/usr/bin/python
# ruff: noqa: F401
import itertools
import sys
from collections import Counter, defaultdict, deque
from copy import deepcopy
from heapq import heappop, heappush
from math import lcm

fn = sys.argv[1] if len(sys.argv) > 1 else '8.in'
with open(fn) as f:
    G = data = f.read().strip().split('\n')
R = len(G)
C = len(G[0])
DR = [1, -1, 1, -1]
DC = [1, -1, -1, 1]
P = defaultdict(list)
for r in range(R):
    for c in range(C):
        s = G[r][c]
        if s != '.':
            P[s].append((r, c))


def f(a, b):
    ax, ay = a
    bx, by = b
    for r in range(R):
        for c in range(C):
            dx = abs(ax-r)
            dy = abs(ay-c)
            for i in range(4):
                xx = bx+dx*2*DR[i]
                yy = by+dy*2*DC[i]
                xxx = ax+dx*DR[i]
                yyy = ay+dy*DC[i]
                if (xxx, yyy) == (xx, yy) == (r, c):
                    yield (r, c)


def g(a, b):
    ax, ay = a
    bx, by = b
    dx = ax-bx
    dy = ay-by
    rr, cc = a
    while True:
        rr += dx
        cc += dy
        if 0 <= rr < R and 0 <= cc < C:
            yield (rr, cc)
        else:
            break


A = set()
B = set()
for t, points in P.items():
    for pa, pb in itertools.combinations(points, 2):
        for a, b in (pa, pb), (pb, pa):
            A.update(f(a, b))
            B.update((a, b))
            B.update(g(a, b))
print('A', len(A))
print('B', len(B))
