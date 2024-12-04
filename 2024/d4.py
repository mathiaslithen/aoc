#!/usr/bin/python
# ruff: noqa: F401
import sys
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from math import lcm

fn = sys.argv[1] if len(sys.argv) > 1 else '4.in'
with open(fn) as f:
    G = data = f.read().strip().split('\n')
R = len(G)
C = len(G[0])
DR = [1, -1, 0, 0, 1, -1, 1, -1]
DC = [0, 0, 1, -1, 1, -1, -1, 1]
A = 0
for r in range(R):
    for c in range(C):
        if G[r][c] == 'X':
            for dr, dc in zip(DR, DC):
                word = 'X'
                _r = r
                _c = c
                for _ in range(3):
                    rr = _r + dr
                    cc = _c + dc
                    if 0 <= rr < R and 0 <= cc < C:
                        word += G[rr][cc]
                    _r = rr
                    _c = cc
                if word == 'XMAS':
                    A += 1
print(A)
DR = [1, -1, 1, -1]
DC = [1, -1, -1, 1]
B = 0
for r in range(R):
    for c in range(C):
        if G[r][c] == 'A':
            word = ''
            for ix in range(4):
                rr = r + DR[ix]
                cc = c + DC[ix]
                if 0 <= rr < R and 0 <= cc < C:
                    word += G[rr][cc]
            if word in ('SMMS', 'MSSM', 'MSMS', 'SMSM'):
                B += 1
print(B)
