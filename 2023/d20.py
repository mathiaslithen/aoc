#!/usr/bin/python
import collections
import copy
import math
import sys

fn = sys.argv[1] if len(sys.argv) > 1 else '20.in'
with open(fn) as f:
    data = f.read().strip()
lines = data.split('\n')


# {name: [type, state, neighbours]}
M = {}
for line in lines:
    module, neighbours = line.split(' -> ')
    neighbours = neighbours.split(', ')
    if module[0] == '%':
        mtype = 0
        name = module[1:]
        state = 0
    elif module[0] == '&':
        mtype = 1
        name = module[1:]
        state = {}
    elif module[0] == 'b':
        mtype = 2
        name = module
        state = None
    M[name] = [mtype, state, neighbours]

# init nand gates to 0
for mod in M:
    for n in M[mod][-1]:
        if n in M and M[n][0] == 1:
            M[n][1][mod] = 0

# find nand controlling rx
for mod in M:
    if M[mod][-1] == ['rx']:
        master_nand = mod
        break
master_nand_inputs = len([mod for mod in M if master_nand in M[mod][-1]])


def f(root, presses, M, part=1):
    LOW = 0
    HIGH = 0
    cycles = {}
    for p in range(1, presses+1):
        Q = collections.deque([root])
        while Q:
            sender, hilow, dst = Q.popleft()
            if hilow == 1:
                HIGH += 1
            elif hilow == 0:
                LOW += 1
            else:
                assert False
            if dst not in M:
                continue
            if dst == master_nand and hilow == 1:
                if sender not in cycles:
                    cycles[sender] = p
            # %
            if M[dst][0] == 0 and hilow == 0:
                M[dst][1] ^= 1
                for x in M[dst][-1]:
                    Q.append((dst, M[dst][1], x))
            # &
            elif M[dst][0] == 1:
                M[dst][1][sender] = hilow
                b = 0 if all(M[dst][1].values()) else 1
                for x in M[dst][-1]:
                    Q.append((dst, b, x))
            # broadcaster
            elif M[dst][0] == 2:
                for x in M[dst][-1]:
                    Q.append((dst, hilow, x))
        if part == 2 and len(cycles) == master_nand_inputs:
            break
    if part == 1:
        return HIGH * LOW
    return math.lcm(*cycles.values())


S = (None, 0, 'broadcaster')
N = copy.deepcopy(M)
print('part1:', f(S, 1000, M))
print('part2:', f(S, 10**10, N, part=2))
