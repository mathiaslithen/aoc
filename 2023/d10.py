#!/usr/bin/python
import sys
from collections import deque

fn = sys.argv[1] if len(sys.argv) > 1 else '10.in'
with open(fn) as f:
    data = f.read().strip()
lines = data.split('\n')
G = [[x for x in line] for line in lines]
R = len(G)
C = len(G[0])
for row in range(R):
    for col in range(C):
        if G[row][col] == 'S':
            START = (row, col)
            break
dirs = {
    # row up/down flipped
    '|': ((1, 0), (-1, 0)),
    '-': ((0, -1), (0, 1)),
    'L': ((-1, 0), (0, 1)),
    'J': ((-1, 0), (0, -1)),
    '7': ((1, 0), (0, -1)),
    'F': ((1, 0), (0, 1)),
    'S': ((1, 0), (-1, 0), (0, 1), (0, -1))
}
shapes = {
    '|': ((0, 1), (1, 1), (2, 1)),
    '-': ((1, 0), (1, 1), (1, 2,)),
    'L': ((0, 1), (1, 1), (1, 2)),
    'J': ((1, 0), (1, 1), (0, 1)),
    '7': ((1, 0), (1, 1), (2, 1)),
    'F': ((1, 2), (1, 1), (2, 1)),
}
moves = {
    'up': ('|', '7', 'F', 'S'),
    'down': ('|', 'L', 'J', 'S'),
    'left': ('-', 'L', 'F', 'S'),
    'right': ('-', '7', 'J', 'S'),
}
can_move = {
    'up': {'|', 'L', 'J'},
    'down': {'|', '7', 'F'},
    'left': {'-', 'J', '7'},
    'right': {'-', 'L', 'F'},
}

starters = {x for x in dirs if x != 'S'}
root = [START]
seen = set()
Q = deque(root)
while Q:
    pos = Q.popleft()
    row, col = pos
    val = G[row][col]
    for dr, dc in dirs[val]:
        rr = row + dr
        cc = col + dc
        n = (rr, cc)
        nxt = G[rr][cc]
        in_bound = 0 <= rr < R and 0 <= cc < C
        valid = in_bound and n not in seen
        # UP
        if valid and dr == -1 and nxt in moves['up']:
            if val == 'S':
                starters &= can_move['up']
            Q.append(n)
            seen.add(n)
        # DOWN
        if valid and dr == 1 and nxt in moves['down']:
            if val == 'S':
                starters &= can_move['down']
            Q.append(n)
            seen.add(n)
        # LEFT
        if valid and dc == -1 and nxt in moves['left']:
            if val == 'S':
                starters &= can_move['left']
            Q.append(n)
            seen.add(n)
        # RIGHT
        if valid and dc == 1 and nxt in moves['right']:
            if val == 'S':
                starters &= can_move['right']
            Q.append(n)
            seen.add(n)
loop = seen
print('part 1:', len(loop)//2)

# part 2
row, col = START
G[row][col] = starters.pop()

# grid -> 3*grid
RR = R * 3
CC = C * 3
EMPTY = '.'
WALL = '#'
GG = [[EMPTY for _ in range(CC)] for _ in range(RR)]
for row in range(R):
    for col in range(C):
        val = G[row][col]
        if val == '.':
            continue
        rr = 3 * row
        cc = 3 * col
        for x, y in shapes[val]:
            GG[rr + x][cc + y] = WALL

s = set()
for row in range(RR):
    s.add((row, 0))
    s.add((row, CC - 1))
for col in range(CC):
    s.add((0, col))
    s.add((RR - 1, col))
root = list(s)

void = set()
seen = set()
Q = deque(root)
while Q:
    pos = Q.popleft()
    if pos in seen:
        continue
    seen.add(pos)
    row, col = pos
    if GG[row][col] == WALL:
        continue
    else:
        void.add(pos)
    for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        rr = row + dr
        cc = col + dc
        n = (rr, cc)
        if 0 <= rr < RR and 0 <= cc < CC and n not in seen:
            Q.append(n)

enc = 0
for row in range(R):
    for col in range(C):
        outside = False
        for dr in range(3):
            for dc in range(3):
                rr = 3 * row + dr
                cc = 3 * col + dc
                n = (rr, cc)
                if n in void:
                    outside = True
        if not outside:
            enc += 1
print('part 2:', enc)
