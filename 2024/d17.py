#!/usr/bin/pypy3
# ruff: noqa: F401
import functools
import math
import sys
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush

from helpers import ALLD, DIAG, DIM, DRC, GFIND, INB, INTS, RC, ROT, VIS

sys.setrecursionlimit(10**5)
fn = sys.argv[1] if len(sys.argv) > 1 else '17.in'
with open(fn) as f:
    data = f.read().strip()


def parse(data):
    reg, prog = data.split('\n\n')
    r = []
    for line in reg.split('\n'):
        r.append(int(line.split(':')[1]))
    prog = list(map(int, prog.split(':')[1].split(',')))
    return r, prog


def f(reg, prog):
    ans = []
    (rxa, rxb, rxc) = reg

    def combo(o):
        return [0, 1, 2, 3, rxa, rxb, rxc][o]

    PC = 0
    while PC < len(prog)-1:
        opc, op = prog[PC:PC+2]
        if opc == 0:
            rxa = rxa // 2**combo(op)
        elif opc == 1:
            rxb ^= op
        elif opc == 2:
            rxb = combo(op) % 8
        elif opc == 3 and rxa:
            PC = op
            continue
        elif opc == 4:
            rxb ^= rxc
        elif opc == 5:
            ans.append(combo(op) % 8)
        elif opc == 6:
            rxb = rxa // (2**combo(op))
        elif opc == 7:
            rxc = rxa // (2**combo(op))
        PC += 2
    return ans


def rev(a, b, c, target):
    """
    Register A: 46323429
    Register B: 0
    Register C: 0

    Program: 2,4, 1,1, 7,5, 1,5, 4,3, 0,3, 5,5, 3,0
    b = a % 8
    b = b ^ 1
    c = a / 2**b
    b = b ^ 5
    b = b ^ c
    a = a / 8
    out(b % 8)
    if a != 0: loop
    """
    reg = (a, b, c)
    out = []
    while a:
        b = a % 8
        b = b ^ 1
        c = a // (2 ** b)
        b = b ^ 5
        b = b ^ c
        a = a // 8
        out.append(b % 8)
    return out == target, reg, out


def p2(data):
    reg, prog = parse(data)
    for i in range(20567627247056 << 3, 10**20):
        t, r, o = rev(i, 0, 0, prog)
        if t:
            # print(f'success @ {i=} -> {r=} & {o=}')
            return r[0]


def p1(data):
    return ','.join(map(str, f(*parse(data))))


print('A', p1(data))
print('B', p2(data))
