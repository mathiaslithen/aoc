#!/usr/bin/python
# ruff: noqa: F401
import sys
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from math import lcm

fn = sys.argv[1] if len(sys.argv) > 1 else 'n.in'
with open(fn) as f:
    data = f.read().strip()
lines = data.split('\n')
