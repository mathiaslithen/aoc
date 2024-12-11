#!/usr/bin/pypy3
# ruff: noqa: F401
import sys
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from math import lcm

fn = sys.argv[1] if len(sys.argv) > 1 else '10.in'
with open(fn) as f:
    data = f.read().strip()
G = [list(map(int, line)) for line in data.splitlines()]
R = len(G)
C = len(G[0])
DR = [0, 0, 1, -1]
DC = [1, -1, 0, 0]


def get_start(G):
    start = []
    for r in range(R):
        for c in range(C):
            if G[r][c] == 0:
                start.append((((r, c), None), ((r, c),)))
    return start


def f(G, part=1):
    start = get_start(G)
    Q = deque(start)
    FP = defaultdict(int)
    seen = set()
    while Q:
        key, path = Q.pop()
        if len(path) == 10 and key not in seen:
            if part == 2:
                key = key[0]
            FP[key] += 1
            seen.add(key)
            continue
        r, c = path[-1]
        for i in range(4):
            rr = DR[i] + r
            cc = DC[i] + c
            if 0 <= rr < R and 0 <= cc < C and G[rr][cc] == G[r][c]+1 and (rr, cc) not in path:
                Q.append(((key[0], (rr, cc)), tuple((*path, (rr, cc)))))
    return sum(FP.values())


print('A', f(G))
print('B', f(G, part=2))
