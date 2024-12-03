#!/usr/bin/python
import sys

fn = sys.argv[1] if len(sys.argv) > 1 else '2.in'
with open(fn) as f:
    data = f.read().strip()
lines = data.split('\n')
A = B = 0
for line in lines:
    d = [line[i] - line[i+1] for i in range(len(line)-1)]
    if all(i in (1, 2, 3) for i in d) or all(i in (-1, -2, -3) for i in d):
        A += 1
    for ix in range(len(line)):
        _line = [x for i, x in enumerate(line) if i != ix]
        xx = [_line[i] - _line[i+1] for i in range(len(_line)-1)]
        if all(i in (1, 2, 3) for i in xx) or all(i in (-1, -2, -3) for i in xx):
            B += 1
            break
print(A)
print(B)
