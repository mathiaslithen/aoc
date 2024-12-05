#!/usr/bin/python
# ruff: noqa: F401
import sys
from collections import Counter, defaultdict, deque
from functools import cmp_to_key
from heapq import heappop, heappush
from math import lcm

fn = sys.argv[1] if len(sys.argv) > 1 else '5.in'
with open(fn) as f:
    data = f.read().strip()

inst, rows = data.split('\n\n')
OR = []
for row in inst.splitlines():
    OR.append(list(map(int, row.split('|'))))
G = []
for row in rows.splitlines():
    G.append(list(map(int, row.split(','))))


def f(this, other):
    for a, b in OR:
        if this == a and other == b:
            return -1
        if this == b and a == other:
            return 1


A = B = 0
for ix, row in enumerate(G):
    rr = sorted(row, key=cmp_to_key(f))
    if G[ix] == rr:
        A += rr[len(rr)//2]
    if G[ix] != rr:
        B += rr[len(rr)//2]
print(A)
print(B)
