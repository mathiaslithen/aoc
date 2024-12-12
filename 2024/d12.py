#!/usr/bin/pypy3
# ruff: noqa: F401
import sys
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from math import lcm

sys.setrecursionlimit(10**5)
fn = sys.argv[1] if len(sys.argv) > 1 else '12.in'
with open(fn) as f:
    data = f.read().strip()
G = data.splitlines()
R = len(G)
C = len(G[0])
DR = [0, 0, 1, -1]
DC = [1, -1, 0, 0]


def f(G, part=1):
    seen = set()
    ans = 0
    for r in range(R):
        for c in range(C):
            p = (r, c)
            if p in seen:
                continue
            seen.add(p)
            soil = G[r][c]
            plot = get_plot(G, p, soil, seen)
            perimiter = get_perimiter_a(G, plot)
            if part == 1:
                X = len(perimiter)
            else:
                X = get_corners(G, perimiter, plot)
            ans += len(plot) * X
    return ans


def get_plot(G, p, soil, seen):
    Q = deque([p])
    plot = []
    while Q:
        p = Q.pop()
        r, c = p
        plot.append(p)
        for dr, dc in zip(DR, DC):
            rr = r + dr
            cc = c + dc
            np = (rr, cc)
            if 0 <= rr < R and 0 <= cc < C and G[rr][cc] == soil and np not in seen:
                Q.append(np)
                seen.add(np)
    return plot


def get_corners(G, permiter, plot):
    if len(plot) in (1, 2):
        return 4
    ans = 0
    for p in plot:
        r, c = p
        neig = []
        for dr, dc in zip(DR, DC):
            rr = r + dr
            cc = c + dc
            np = (rr, cc)
            if np in plot:
                neig.append(np)
        if len(neig) == 1:
            ans += 2
        if len(neig) == 2:
            if not (neig[0][0] == neig[1][0] or neig[0][1] == neig[1][1]):
                ans += 1
    perims = {p for _, p in permiter}
    for p in perims:
        r, c = p
        for dr, dc in ((1, 1), (-1, -1), (-1, 1), (1, -1)):
            rr = r + dr
            cc = c + dc
            np = (rr, cc)
            if np in plot and (r, cc) in plot and (rr, c) in plot:
                ans += 1
    return ans


def get_perimiter_a(G, plot):
    permiter = set()
    seen = set(plot)
    for p in plot:
        r, c = p
        for dr, dc in zip(DR, DC):
            rr = r + dr
            cc = c + dc
            np = (rr, cc)
            if np in seen:
                continue
            permiter.add((p, np))
    return permiter


print('A', f(G))
print('B', f(G, part=2))
