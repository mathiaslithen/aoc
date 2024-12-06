#!/usr/bin/python
# ruff: noqa: F401
import sys
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from math import lcm

fn = sys.argv[1] if len(sys.argv) > 1 else '6.in'
with open(fn) as f:
    data = f.read().strip().split('\n')
G = set()
R = len(data)
C = len(data[0])
S = None
dir = (-1, 0)
dirs = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
}
for r in range(R):
    for c in range(C):
        if data[r][c] == '#':
            G.add((r, c))
        if data[r][c] == '^':
            S = (r, c)
SS = S
seen = set()
seen.add(S)
steps = 0
while True:
    r, c = S
    dr, dc = dir
    rr = r + dr
    cc = c + dc
    if (rr, cc) in G:
        dir = dirs[dir]
        continue
    if 0 <= rr < R and 0 <= cc < C:
        steps += 1
        seen.add((rr, cc))
        S = (rr, cc)
    else:
        break
print('A', len(seen))
B = 0
for sr in range(R):
    for sc in range(C):
        S = SS
        ddir = -1, 0
        if (sr, sc) in G or (sr, sc) == S:
            continue
        GG = set(x for x in G)
        GG.add((sr, sc))
        seen = set()
        while True:
            r, c = S
            dr, dc = ddir
            rr = r + dr
            cc = c + dc
            if (rr, cc) in GG:
                if (ddir, r, c) in seen:
                    B += 1
                    break
                seen.add((ddir, r, c))
                ddir = dirs[ddir]
                continue
            if 0 <= rr < R and 0 <= cc < C:
                S = (rr, cc)
            else:
                break
print('B', B)
