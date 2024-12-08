#!/usr/bin/python
# ruff: noqa: F401
import itertools
import sys
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from math import lcm
from operator import add, mul

fn = sys.argv[1] if len(sys.argv) > 1 else '7.in'
with open(fn) as f:
    data = f.readlines()
G = {}
for line in data:
    res, ints = line.split(':')
    res = int(res)
    ints = list(map(int, ints.split()))
    G[res] = ints


def f(ints, ops, v=None):
    if not ints:
        yield v
    elif v is None:
        yield from f(ints[1:], ops, ints[0])
    else:
        for o in ops:
            yield from f(ints[1:], ops, o(v, ints[0]))


A = B = 0
for ans, ints in G.items():
    for v in f(ints, (add, mul)):
        if v == ans:
            A += ans
            break
    for v in f(ints, (add, mul, lambda x,y: int(str(x)+str(y)))):
        if v == ans:
            B += ans
            break
print('A', A)
print('B', B)
