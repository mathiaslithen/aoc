#!/usr/bin/pypy3
# ruff: noqa: F401
import copy
import sys
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from math import lcm

fn = sys.argv[1] if len(sys.argv) > 1 else '9.in'
with open(fn) as f:
    data = list(map(int, f.read().strip()))


def vis(blocks):
    return ''.join(str('.' if s is None else s) for s in blocks)


def get_blocks(data):
    blocks = []
    i = 0
    for ix, n in enumerate(data):
        if ix % 2 == 0:
            blocks += [i]*n
            i += 1
        else:
            blocks += [None]*n
    return blocks, i


def get_free(blocks, part=1):
    if part == 1:
        return [ix for ix, n in enumerate(blocks) if n is None]
    free = {}  # ix: length
    last = None
    for ix, n in enumerate(blocks):
        if n is None and not last:
            free[ix] = 1
            last = ix
            continue
        elif last and n is None:
            free[last] += 1
        else:
            last = None
    return free


def chk(blocks):
    ans = 0
    for ix, n in enumerate(blocks):
        if n is not None:
            ans += ix*n
    return ans


def a(data):
    blocks, _ = get_blocks(data)
    free = get_free(blocks)
    for ix in free:
        while blocks[-1] is None:
            blocks.pop()
        if ix >= len(blocks)-1:
            break
        blocks[ix] = blocks.pop()
    return chk(blocks)


def b(data):
    blocks, ID = get_blocks(data)
    free = get_free(blocks, part=2)
    pos = len(blocks) - 1
    G = blocks[:]
    for ix in reversed(range(ID)):
        while pos and blocks[pos] != ix:
            pos -= 1
        length = 0
        if blocks[pos] == ix:
            length = 1
            while True:
                pos -= 1
                if blocks[pos] == ix:
                    length += 1
                else:
                    break
        if length:
            for idx, free_length in free.items():
                if idx < pos and free_length >= length:
                    for j in range(length):
                        G[idx + j] = ix
                        G[pos+1+j] = None
                    break
            free = get_free(G, part=2)
    return chk(G)


print('A', a(data))
print('B', b(data))
