#!/usr/bin/pypy3
# ruff: noqa: F401
import functools
import sys
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from math import lcm

from helpers import ALLD, DIAG, DRC, GFIND, INB, INTS, RC

sys.setrecursionlimit(10**5)
fn = sys.argv[1] if len(sys.argv) > 1 else '14.in'
with open(fn) as f:
    data = f.read().strip()
R, C = 103, 101
# R, C = 7, 11


def vis(pos):
    g = [[0 for c in range(C)] for r in range(R)]
    for p in pos:
        r, c = p
        g[r][c] += 1
    print('\n'.join(''.join(str('.' if x == 0 else x) for x in line) for line in g), '\n')


def parse(data):
    pos = []
    vel = []
    for line in data.splitlines():
        c, r, vc, vr = INTS(line)
        pos.append((r, c))
        vel.append((vr, vc))
    return pos, vel


def move(p, v):
    r, c = p
    dr, dc = v
    rr, cc = (r + dr) % R, (c + dc) % C
    return (rr, cc)


def cal(pos):
    X = []
    x = (
        (0, R//2, 0, C//2),
        (0, R//2, 1+(C//2), C),
        (1+(R//2), R, 0, C//2),
        (1+(R//2), R, 1+(C//2), C),
    )
    for rmi, rma, cmi, cma in x:
        t = 0
        for p in pos:
            r, c = p
            if rmi <= r < rma and cmi <= c < cma:
                t += 1
        X.append(t)
    ans = 1
    for i in X:
        ans *= i
    return ans


def search(pos):
    N = 20
    for r in range(R):
        x = list(sorted([cc for rr, cc in pos if rr == r]))
        if len(x) < N:
            continue
        for i in range(len(x)):
            if all(j+i in x for j in range(N)):
                return True


def g(data):
    pos, vel = parse(data)
    sec = 0
    while True:
        sec += 1
        for i in range(len(pos)):
            np = move(pos[i], vel[i])
            pos[i] = np
        if search(pos):
            vis(pos)
            inp = input(f'{sec=} continue (y/n)?')
            if inp == 'n':
                break
    return sec


def f(data):
    pos, vel = parse(data)
    for sec in range(100):
        for i in range(len(pos)):
            np = move(pos[i], vel[i])
            pos[i] = np
    return cal(pos)


print('A', f(data))
print('B', g(data))
