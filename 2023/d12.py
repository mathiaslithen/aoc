#!/usr/bin/python
import functools
import sys

fn = sys.argv[1] if len(sys.argv) > 1 else '12.in'
with open(fn) as f:
    data = f.read().strip()
lines = data.split('\n')


@functools.cache
def f(slots, blocks):
    if not slots:
        if not blocks:
            return 1
        return 0
    if not blocks:
        if '#' not in slots:
            return 1
        return 0

    ret = 0
    val = slots[0]
    block_len = blocks[0]
    available_slots = slots[0:block_len]
    next_slot = slots[block_len:block_len+1]

    if val in ('.', '?'):
        ret += f(slots[1:], blocks)

    if val in ('#', '?'):
        if (
            len(available_slots) == block_len
            and '.' not in available_slots
            and next_slot != '#'
        ):
            ret += f(slots[block_len+1:], blocks[1:])

    return ret


a = []
b = []
for line in lines:
    slots, blocks = line.split()
    blocks = tuple(int(x) for x in blocks.split(','))
    a.append(f(slots, blocks))
    slots = '?'.join(slots for _ in range(5))
    blocks = blocks*5
    b.append(f(slots, blocks))
print(sum(a))
print(sum(b))
