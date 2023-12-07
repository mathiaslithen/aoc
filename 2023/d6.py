#!/usr/bin/python
import sys

fn = sys.argv[1] if len(sys.argv) > 1 else '6.in'
with open(fn) as f:
    data = f.read().strip()
lines = data.split('\n')
T = [int(i) for i in lines[0].split() if i.isnumeric()]
D = [int(i) for i in lines[1].split() if i.isnumeric()]
A = 1
for t, d in zip(T, D):
    x = 0
    i = 0
    while True:
        if i >= t-1:
            break
        v = i
        race = v*(t-v)
        if race > d:
            x += 1
        i += 1
    A *= x
print(A)

t = int(''.join(str(i) for i in T))
d = int(''.join(str(i) for i in D))
i = 0
B = 0
while True:
    if i >= t-1:
        break
    v = i
    race = v*(t-v)
    if race > d:
        B += 1
    i += 1
print(B)
