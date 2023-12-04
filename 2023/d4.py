#!/usr/bin/python
import sys
from collections import defaultdict

fn = sys.argv[1] if len(sys.argv) > 1 else '4.in'
with open(fn) as f:
    data = f.read().strip()
lines = data.split('\n')

A = 0
B = defaultdict(int)
for i, line in enumerate(lines):
    _, cards = line.split(':')
    a, b = cards.split('|')
    a = set(int(i) for i in a.split())
    b = set(int(i) for i in b.split())
    wins = len(a.intersection(b))
    p = 0.5
    B[i] += 1
    for w in range(wins):
        p *= 2
        next_card = i + w + 1
        B[next_card] += B[i]
    if p >= 1:
        A += p
print(int(A))
print(sum(B.values()))
