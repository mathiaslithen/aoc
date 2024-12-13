#!/usr/bin/python3
# ruff: noqa: F401
import functools
import sys
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from math import lcm

import numpy as np

from helpers import ALLD, DIAG, DRC, GFIND, INB, INTS, RC

sys.setrecursionlimit(10**5)
fn = sys.argv[1] if len(sys.argv) > 1 else '13.in'
with open(fn) as f:
    G = data = f.read().strip()

K = 10000000000000


def parse(data):
    G = []
    for segment in data.split('\n\n'):
        G.append([INTS(line) for line in segment.split('\n')])
    return G


def calc(S, part=1):
    x1, x2, xr = S[0][0], S[1][0], S[2][0]+(0 if part == 1 else K)
    y1, y2, yr = S[0][1], S[1][1], S[2][1]+(0 if part == 1 else K)
    arr1 = np.array([[x1, x2], [y1, y2]])
    arr2 = np.array([xr, yr])
    res = np.linalg.solve(arr1, arr2)
    # a, b = map(int, res)
    a, b = map(round, res)
    if a >= 0 and b >= 0 and a*x1 + b*x2 == xr and a*y1 + b*y2 == yr:
        yield a*3 + b


def f(G, part=1):
    G = parse(G)
    ans = 0
    for S in G:
        ans += sum(calc(S, part=part))
    return ans


print('A', f(G))
print('B', f(G, part=2))
