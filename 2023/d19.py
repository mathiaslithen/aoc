#!/usr/bin/python
import collections
import sys

fn = sys.argv[1] if len(sys.argv) > 1 else '19.in'
with open(fn) as f:
    data = f.read().strip()
workflows, ratings = data.split('\n\n')


xmas = dict((v, i) for i, v in enumerate('xmas'))


def f(WF, R):
    ret = 0
    ops = {
        '>': lambda x, y: x > y,
        '<': lambda x, y: x < y,
    }
    S = 'in'
    for rating in R:
        name = S
        while name not in 'AR':
            instructions = WF[name]
            for inst in instructions:
                if isinstance(inst, str):
                    name = inst
                else:
                    left, op, right, nxt = inst
                    if ops[op](rating[left], right):
                        name = nxt
                        break
            if name == 'A':
                ret += sum(rating.values())
    return ret


def g(WF):
    ret = []
    Q = collections.deque([('in', [range(1, 4000+1)]*4)])
    while Q:
        name, ranges = Q.popleft()
        if name == 'A':
            ret.append(score(ranges))
            continue
        if name == 'R':
            continue
        instructions = WF[name]
        for inst in instructions[:-1]:
            range_index, op, right, nxt = inst
            rng = ranges[range_index]
            if right not in rng:
                continue
            i = 1 if op == '>' else 0
            ra = range(rng.start, right+i)
            rb = range(right+i, rng.stop)
            if op == '>':
                ra, rb = rb, ra
            nr = ranges[:]
            nr[range_index] = ra
            Q.append((nxt, nr))
            ranges[range_index] = rb
        Q.append((instructions[-1], ranges))
    return sum(ret)


def score(ranges):
    ret = 1
    for r in ranges:
        ret *= len(r)
    return ret


def parse_r(ratings):
    ret = []
    for line in ratings.split('\n'):
        d = {}
        for x in line.strip('{}').split(','):
            k, v = x.split('=')
            d[xmas[k]] = int(v)
        ret.append(d)
    return ret


def parse_w(workflows):
    ret = {}
    for line in workflows.split('\n'):
        name, instructions = line.split('{')
        instructions = instructions.strip('}').split(',')
        l = []
        for i in instructions:
            if ':' in i:
                left = i[0]
                op = i[1]
                right, nxt = i[2:].split(':')
                l.append((xmas[left], op, int(right), nxt))
            else:
                l.append(i)
        ret[name] = l
    return ret


WF = parse_w(workflows)
R = parse_r(ratings)
print('part1:', f(WF, R))
print('part2:', g(WF))
