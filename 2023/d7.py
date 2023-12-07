#!/usr/bin/python
import collections
import sys
from functools import cmp_to_key

vals = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
}
types = {
    (5,): 10,
    (1, 4): 9,
    (2, 3): 8,
    (1, 1, 3): 7,
    (1, 2, 2): 6,
    (1, 1, 1, 2): 5,
    (1, 1, 1, 1, 1): 4,
}

fn = sys.argv[1] if len(sys.argv) > 1 else '7.in'
with open(fn) as f:
    data = f.read().strip()
lines = data.split('\n')

X = []
for line in lines:
    a, b = line.split()
    X.append((a, int(b)))


def f(hand, other):
    hand = hand[0]
    other = other[0]
    ch = collections.Counter(hand)
    co = collections.Counter(other)
    # p2
    j = ch.pop('J', 0)
    ch.update({ch.most_common()[0][0] if ch else 'J': j})
    j = co.pop('J', 0)
    co.update({co.most_common()[0][0] if co else 'J': j})
    # /p2
    t_h = types.get(tuple(sorted(ch.values())))
    t_o = types.get(tuple(sorted(co.values())))
    if t_h > t_o:
        return 1
    if t_h < t_o:
        return -1
    for i in range(5):
        x = hand[i]
        y = other[i]
        # p1
        # xx = int(vals.get(x, x))
        # yy = int(vals.get(y, y))
        # /p1
        # p2
        xx = -1 if x == 'J' else int(vals.get(x, x))
        yy = -1 if y == 'J' else int(vals.get(y, y))
        # /p2
        if xx > yy:
            return 1
        if xx < yy:
            return -1


ans = 0
for rank, x in enumerate(sorted(X, key=cmp_to_key(f))):
    ans += (rank + 1) * x[1]
print(ans)
