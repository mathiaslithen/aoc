#!/usr/bin/python
import collections
import sys

fn = sys.argv[1] if len(sys.argv) > 1 else '1.in'
with open(fn) as f:
    data = f.read().strip()
lines = data.split('\n')
L, R = [], []
rr = collections.defaultdict(int)
for line in lines:
    a, b = map(int, line.split())
    L.append(a)
    R.append(b)
    rr[b] += 1
A = B = 0
for a, b in zip(sorted(L), sorted(R)):
    A += abs(a-b)
    B += a * rr[a]
print(A)
print(B)
