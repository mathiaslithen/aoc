#!/usr/bin/python
import sys

fn = sys.argv[1] if len(sys.argv) > 1 else '11.in'
with open(fn) as f:
    data = f.read().strip()
lines = data.split('\n')
G = [[x for x in line] for line in lines]
# expand
e_rows = set()
e_cols = set()
for col in reversed(range(len(G[0]))):
    if all(row[col] in ('.', 'E') for row in G):
        e_cols.add(col)
for row in reversed(range(len(G))):
    if all(x in ('E', '.') for x in G[row]):
        e_rows.add(row)

g = 1
gal = {}
for row in range(len(G)):
    for col in range(len(G[0])):
        val = G[row][col]
        if val == '#':
            gal[g] = (row, col)
            g += 1
keys = list(gal.keys())
pairs = [(a, b) for i, a in enumerate(keys) for b in keys[i + 1:]]


def f(m):
    m = m - 1
    res = []
    for p in pairs:
        a, b = p
        x1, y1 = gal[a]
        x2, y2 = gal[b]
        dx = x2-x1
        dy = y2-y1
        dx = abs(dx)
        dy = abs(dy)
        mi = min(x1, x2)
        ma = max(x1, x2)
        for c in e_rows:
            if c in range(mi, ma):
                dx += m
        mi = min(y1, y2)
        ma = max(y1, y2)
        for r in e_cols:
            if r in range(mi, ma):
                dy += m
        res.append(dx + dy)
    print(sum(res))


f(2)
f(1000000)
