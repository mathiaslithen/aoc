#!/usr/bin/pypy3
# ruff: noqa: F401
import functools
import sys
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from math import lcm

from helpers import ALLD, DIAG, DIM, DRC, GFIND, INB, INTS, RC, VIS

# keyword: djikstra

sys.setrecursionlimit(10**5)
fn = sys.argv[1] if len(sys.argv) > 1 else '16.in'
with open(fn) as f:
    data = f.read().strip()
G = data.splitlines()


faces = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1),
}


def moves(f):
    if f == 'N':
        return ('N', 'W', 'E')
    if f == 'S':
        return ('S', 'W', 'E')
    if f == 'W':
        return ('W', 'N', 'S')
    if f == 'E':
        return ('E', 'N', 'S')


def f(G, part=1):
    ans = []
    start_pos, = GFIND(G, 'S')
    end_pos, = GFIND(G, 'E')
    walls = GFIND(G, '#')
    seen = set()
    Q = [(0, start_pos, 'E', [])]
    while Q:
        cost, pos, face, path = heappop(Q)
        r, c = pos
        if pos == end_pos:
            ans.append((cost, path))
        seen.add((pos, face))
        for nf in moves(face):
            dr, dc = faces[nf]
            step_cost = 1 if face == nf else 1001
            np = (rr, cc) = r + dr, c + dc
            if INB(G, rr, cc) and np not in walls and (np, nf) not in seen:
                _path = path[:] + [np]
                heappush(Q, (cost+step_cost, np, nf, _path))
    ans.sort()
    if part == 1:
        return ans[0][0]
    best = {start_pos, end_pos}
    for s in [set(p) for i, p in ans if i == ans[0][0]]:
        best = best.union(s)
    return len(best)


print('A', f(G))
print('B', f(G, part=2))
