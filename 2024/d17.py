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
    data = INTS(data)
    return data[:3], data[3:]


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


def rev(a, target):
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
    b = c = 0
    out = []
    while a:
        b = a % 8
        b = b ^ 1
        c = a // (2 ** b)
        b = b ^ 5
        b = b ^ c
        a = a // 8
        out.append(b % 8)
    return out == target


def p2(data):
    reg, prog = parse(data)
    i = p = -1
    while True:
        i += 1
        if rev(i, prog[p:]):
            if p == -16:
                return i
            p -= 1
            i <<= 3


def p1(data):
    return ','.join(map(str, f(*parse(data))))


print('A', p1(data))
print('B', p2(data))
