#!/usr/bin/python
import sys
from heapq import heappop, heappush

fn = sys.argv[1] if len(sys.argv) > 1 else '17.in'
with open(fn) as f:
    data = f.read().strip()
lines = data.split('\n')
G = [[x for x in y] for y in lines]
R = len(G)
C = len(G[0])
DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]


def f(start, end, part=1):
    seen = set()
    losses = []
    Q = [start]
    D = {}
    while Q:
        heat, (row, col), last, steps = heappop(Q)
        if (row, col) == end:
            losses.append(heat)
            continue
        for di in range(4):
            rr = row + DR[di]
            cc = col + DC[di]
            if 0 <= rr < R and 0 <= cc < C:
                n = (rr, cc)
                S = list(steps)
                LS = len(S)
                h = heat + int(G[rr][cc])
                if part == 1:
                    if (
                        S.count(di) >= 3
                        or (last and last == n)
                        or (losses and h > min(losses))
                    ):
                        continue
                    if S and di != S[-1]:
                        S = [di]
                    else:
                        S.append(di)
                else:
                    if (
                        (di in S and LS == 10)
                        or (S and S[-1] != di and LS < 4)
                        or (last and last == n)
                        or (losses and h > min(losses))
                    ):
                        continue
                    if S and di != S[-1]:
                        dr = DR[di]
                        dc = DC[di]
                        if (
                            (dr == 1 and rr > R-4)
                            or (dr == -1 and rr < 4)
                            or (dc == 1 and cc > C-4)
                            or (dc == -1 and cc < 4)
                        ):
                            continue
                        S = [di]
                    else:
                        S.append(di)
                S = tuple(S)
                k = (rr, cc, S)
                if k not in D:
                    D[k] = h
                elif D[k] < h:
                    continue
                x = (h, (rr, cc), (row, col), S)
                if x not in seen:
                    seen.add(x)
                    heappush(Q, x)
    return losses


# heat, pos, last_pos, steps
start = (0, (0, 0), None, [])
end = (R-1, C-1)
print('part 1', min(f(start, end)))
print('part 2', min(f(start, end, part=2)))
