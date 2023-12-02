#!/usr/bin/python
import sys

fn = sys.argv[1] if len(sys.argv) > 1 else '2.in'
with open(fn) as f:
    data = f.read().strip()
lines = data.split('\n')
X = {
    'red': 12,
    'green': 13,
    'blue': 14,
}
r = []
rr = []
for line in lines:
    C = {}
    _, g = line.split(':')[0].split()
    words = line.split(':')[1].split()
    for i, word in enumerate(words):
        if word.isnumeric():
            col = words[i+1].strip(';,')
            C[col] = max(C.get(col, 0), int(word))
    if all(C.get(col, 0) <= amt for col, amt in X.items()):
        r.append(int(g))
    power = 1
    for col in X:
        power *= C.get(col, 1)
    rr.append(power)

print(sum(r))
print(sum(rr))
