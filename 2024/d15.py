#!/usr/bin/pypy3
# ruff: noqa: F401
import functools
import sys
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from math import lcm

from helpers import ALLD, DIAG, DRC, GFIND, INB, INTS, RC

sys.setrecursionlimit(10**5)
fn = sys.argv[1] if len(sys.argv) > 1 else '15.in'
with open(fn) as f:
    data = f.read().strip()


def parse(data, part=1):
    g, i = data.split('\n\n')
    dirs = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
    if part == 1:
        G = g.splitlines()
    else:
        G = []
        for line in g.splitlines():
            line = line.replace('#', '##').replace('.', '..').replace('O', '[]').replace('@', '@.')
            G.append(line)
    inst = []
    for line in i.splitlines():
        for d in line:
            inst.append(dirs[d])
    return G, inst


def gps(boxes):
    ans = 0
    for r, c in boxes:
        ans += r*100 + c
    return ans


def is_box(pos, boxes):
    for le, ri in boxes:
        if pos == le or pos == ri:
            return (le, ri)


def can_move(box, boxes, move, walls):
    le, ri = box
    dr, dc = move
    lr, lc = le
    rr, rc = ri
    if dr == 0:
        if dc > 0:
            side = ri
        else:
            side = le
        nnn = (side[0], side[1]+dc)
        if nnn in walls:
            yield False
        elif nxt := is_box(nnn, boxes):
            yield from can_move(nxt, boxes, move, walls)
        else:
            yield nnn not in walls
    else:
        pos_l = (lr + dr, lc)
        pos_r = (rr + dr, rc)
        if pos_l in walls or pos_r in walls:
            yield False
        else:
            if pos_l in walls or pos_r in walls:
                yield False
            else:
                if pos_l not in walls and pos_r not in walls:
                    yield True
                if nxt_box := is_box(pos_l, boxes):
                    yield from can_move(nxt_box, boxes, move, walls)
                if nxt_box := is_box(pos_r, boxes):
                    yield from can_move(nxt_box, boxes, move, walls)


def move_box(box, boxes, move):
    le, ri = box
    dr, dc = move
    new_le = le[0]+dr, le[1]+dc
    new_ri = ri[0]+dr, ri[1]+dc
    if dr == 0:
        if dc > 0:
            side = ri
        else:
            side = le
        nnn = side[0], side[1]+dc
        if nxt := is_box(nnn, boxes):
            move_box(nxt, boxes, move)
    else:
        if x := is_box(new_ri, boxes):
            move_box(x, boxes, move)
        if x := is_box(new_le, boxes):
            move_box(x, boxes, move)
    boxes.remove(box)
    boxes.append((new_le, new_ri))


def g(data):
    G, inst = parse(data, part=2)
    robot = GFIND(G, '@')[0]
    G = [x.replace('@', '.') for x in G]
    boxes = list(zip(GFIND(G, '['), GFIND(G, ']')))
    walls = GFIND(G, '#')
    for move in inst:
        dr, dc = move
        new_robot = robot[0]+dr, robot[1]+dc
        if new_robot in walls:
            continue
        elif box := is_box(new_robot, boxes):
            if all(can_move(box, boxes, move, walls)):
                move_box(box, boxes, move)
                robot = new_robot
        else:
            robot = new_robot
    return gps([a for a, b in boxes])


def f(data, part=1):
    G, inst = parse(data)
    robot = GFIND(G, '@')[0]
    boxes = GFIND(G, 'O')
    walls = GFIND(G, '#')
    for move in inst:
        dr, dc = move
        r, c = robot
        new_robot = (rr, cc) = r + dr, c + dc
        if new_robot in walls:
            continue
        elif new_robot in boxes:
            next_slot = None
            nxt = new_robot
            while next_slot is None:
                nr, nc = nxt
                nxt_pos = (rr, cc) = nr+dr, nc+dc
                if nxt_pos in boxes:
                    nxt = nxt_pos
                    continue
                elif nxt_pos in walls:
                    break
                else:
                    next_slot = nxt_pos
            if next_slot:
                boxes.remove(new_robot)
                boxes.append(next_slot)
                robot = new_robot
        else:
            robot = new_robot
    return gps(boxes)


print('A', f(data))
print('B', g(data))
