#!/usr/bin/python
import sys

fn = sys.argv[1] if len(sys.argv) > 1 else '13.in'
with open(fn) as f:
    data = f.read().strip()
lines = data.split('\n\n')


def f(P, mul=1, part=1):
    for i in range(1, len(P)):
        L = P[:i][::-1]
        R = P[i:]

        left = L[:len(R)]
        right = R[:len(L)]

        if part == 1:
            if left == right:
                return len(L) * mul
        else:
            SL = set(
                (r, c, col)
                for r, row in enumerate(left)
                for c, col in enumerate(row)
            )
            SR = set(
                (r, c, col)
                for r, row in enumerate(right)
                for c, col in enumerate(row)
            )
            diff = SL.difference(SR)
            if len(diff) == 1:
                return len(L) * mul
    return 0


a = []
b = []
for pattern in lines:
    P = [[x for x in line] for line in pattern.split('\n')]
    a.append(f(P, mul=100))
    b.append(f(P, mul=100, part=2))
    T = [list(x) for x in zip(*P)]
    a.append(f(T))
    b.append(f(T, part=2))
print(sum(a))
print(sum(b))
