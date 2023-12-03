#!/usr/bin/python
import sys
from collections import defaultdict

fn = sys.argv[1] if len(sys.argv) > 1 else '3.in'
with open(fn) as f:
    data = f.read().strip()

G = [line + '.' for line in data.split('\n')]
R = len(G)
C = len(G[0])
dirs = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1)]
A = []
B = defaultdict(list)
for row in range(R):
    s = ''
    touch = False
    gear = None
    for col in range(C):
        val = G[row][col]
        if val.isnumeric():
            if not touch:
                for dr, dc in dirs:
                    rr = row+dr
                    cc = col+dc
                    if 0 <= rr < R and 0 <= cc < C:
                        _v = G[rr][cc]
                        if not _v.isnumeric() and _v != '.':
                            touch = True
                        if _v == '*':
                            gear = (rr, cc)
            s += val
        else:
            if s and touch:
                A.append(int(s))
            if gear:
                B[gear].append(int(s))
            s = ''
            touch = False
            gear = None

print(sum(A))
print(sum(v[0]*v[1] for _, v in B.items() if len(v) == 2))
