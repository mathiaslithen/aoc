#!/usr/bin/python
import sys

fn = sys.argv[1] if len(sys.argv) > 1 else '15.in'
with open(fn) as f:
    data = f.read().strip()


def hash(s):
    ans = 0
    for x in s:
        ans = (ans + ord(x)) * 17 % 256
    return ans


a = b = 0
hm = [dict() for _ in range(256)]
for inst in data.split(','):
    a += hash(inst)

    if '-' in inst:
        op = '-'
        label = inst.split('-')[0]
        rest = ''
    elif '=' in inst:
        op = '='
        w = inst.split('=')
        label = w[0]
        rest = w[1]

    d = hm[hash(label)]
    if op == '=':
        d[label] = rest
    elif op == '-':
        d.pop(label, None)
    else:
        assert False, inst

for i, box in enumerate(hm):
    if not box:
        continue
    ans = 0
    for n, k in enumerate(box):
        ans += (i+1) * (n+1) * int(box[k])
    b += ans

print(a)
print(b)
