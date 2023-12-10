#!/usr/bin/python
import sys

fn = sys.argv[1] if len(sys.argv) > 1 else '9.in'
with open(fn) as f:
    data = f.read().strip()
lines = data.split('\n')
A = []
B = []
for line in lines:
    his = [int(i) for i in line.split()]
    S = [his]
    while True:
        diff = []
        for i in range(1, len(S[-1])):
            diff.append(S[-1][i] - S[-1][i-1])
        S.append(diff)
        if all(x == 0 for x in diff):
            break
    a = 0
    for x in S[:-1]:
        a += x[-1]
    A.append(a)
    S = list(reversed(S))
    b = 0
    for x in S[1:]:
        b = x[0] - b
    B.append(b)

print(sum(A))
print(sum(B))


# recursive solution


def recurse(xs, p=1):
    if all(x == 0 for x in xs):
        return 0
    diff = [b - a for a, b in zip(xs, xs[1:])]
    if p == 1:
        return xs[-1] + recurse(diff)
    return xs[0] - recurse(diff, p=p)


x = y = 0
for line in lines:
    xs = [int(x) for x in line.split()]
    x += recurse(xs)
    y += recurse(xs, p=2)
print(x)
print(y)
