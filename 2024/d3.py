#!/usr/bin/python
import re
import sys

fn = sys.argv[1] if len(sys.argv) > 1 else '3.in'
with open(fn) as f:
    data = f.read().strip()

r = re.compile(r'mul\(\d{1,3},\d{1,3}\)')


def mul(a, b):
    return a*b


x = r.findall(data)
A = sum(eval(exp) for exp in x)
print(A)

B = 0
S = ''
for ix, exp in enumerate(data.split("don't()")):
    if ix == 0:
        S += exp
        continue
    exp = exp.split('do()')
    S += ''.join(exp[1:])
x = r.findall(S)
B = sum(eval(exp) for exp in x)
print(B)
