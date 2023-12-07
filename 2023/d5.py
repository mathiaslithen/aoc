#!/usr/bin/python
import sys
from collections import defaultdict

fn = sys.argv[1] if len(sys.argv) > 1 else '5.in'
with open(fn) as f:
    data = f.read().strip()

lines = data.split('\n\n')
N = len(lines)-1
seeds = [int(i) for i in lines[0].split(':')[1].split()]

D = defaultdict(list)
for i, line in enumerate(lines[1:]):
    for row in line.split('\n')[1:]:
        dst, src, le = [int(x) for x in row.split()]
        D[i].append((dst, src, le))

A = []
for seed in seeds:
    for i in range(N):
        rows = D[i]
        path = []
        for row in rows:
            dst, src, le = row
            src_max = src + le
            delta = dst - src
            if seed >= src and seed <= src_max:
                path.append(seed + delta)
                break
        else:
            path.append(seed)
        seed = path[-1]
    A.append(path)
print(min(x[-1] for x in A))

# part 2
_seeds = []
for i in range(0, len(seeds), 2):
    a = seeds[i]
    b = seeds[i+1]
    _seeds.append((a, a+b))
seeds = _seeds

for i in range(N):
    rows = D[i]
    path = []
    while seeds:
        start, end = seeds.pop()
        for dst, src, le in rows:
            src_max = src + le
            delta = dst - src
            x = max(start, src)
            y = min(end, src_max)
            if x < y:
                xx = x + delta
                yy = y + delta
                # in range
                path.append((xx, yy))
                # under
                if start < x:
                    seeds.append((start, x))
                # over
                if end > y:
                    seeds.append((y, end))
                break
        else:
            path.append((start, end))
    seeds = path
print(min(x[0] for x in seeds))
