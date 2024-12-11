#!/usr/bin/pypy3
# ruff: noqa: F401
import functools
import sys
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from math import lcm

fn = sys.argv[1] if len(sys.argv) > 1 else '11.in'
with open(fn) as f:
    data = f.read().strip()
G = list(map(int, data.split()))


@functools.cache
def f(blinks, val):
    b = blinks - 1
    if not blinks:
        return 1
    if val == 0:
        return f(b, 1)
    elif len(str(val)) % 2 == 0:
        s = str(val)
        x, y = int(s[:len(s)//2]), int(s[len(s)//2:])
        return f(b, x) + f(b, y)
    return f(b, val*2024)

print('A', sum(f(25, i) for i in G))
print('B', sum(f(75, i) for i in G))
