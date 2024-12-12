#!/usr/bin/pypy3
# ruff: noqa: F401
import functools
import sys
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from math import lcm

from helpers import ALLD, DIAG, DRC, GFIND, INB, INTS, RC

sys.setrecursionlimit(10**5)
fn = sys.argv[1] if len(sys.argv) > 1 else 'n.in'
with open(fn) as f:
    data = f.read().strip()
G = data.splitlines()
R = len(G)
C = len(G[0])


def f(G, part=1):
    print(G)


print('A', f(G))
print('B', f(G, part=2))
