#!/usr/bin/pypy3
# ruff: noqa: F401
import sys
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from math import lcm

sys.setrecursionlimit(10**5)
fn = sys.argv[1] if len(sys.argv) > 1 else 'n.in'
with open(fn) as f:
    data = f.read().strip()
G = data.splitlines()
R = len(G)
C = len(G[0])
