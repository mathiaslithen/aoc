#!/usr/bin/pypy3
# ruff: noqa: F401
import functools
import itertools
import sys
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from math import lcm

from helpers import ALLD, DIAG, DIM, DRC, GFIND, INB, INTS, RC, ROT, VIS

sys.setrecursionlimit(10**5)
fn = sys.argv[1] if len(sys.argv) > 1 else '19.in'
with open(fn) as f:
    pat, towels = data = f.read().strip().split('\n\n')
pat = tuple(pat.split(', '))
towels = towels.splitlines()


@functools.cache
def check(t, part=1):
    ret = 0
    if not t:
        ret += 1
    for p in pat:
        if part == 1 and t.startswith(p) and check(t.removeprefix(p), part=part):
            return 1
        elif part == 2 and t.startswith(p):
            ret += check(t.removeprefix(p), part=part)
    return ret


print('A', sum(check(t) for t in towels))
print('B', sum(check(t, part=2) for t in towels))
