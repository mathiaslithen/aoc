#!/usr/bin/python
import sys

fn = sys.argv[1] if len(sys.argv) > 1 else '1.in'
with open(fn) as f:
    data = f.read().strip()
lines = data.split('\n')

D = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def f(part):
    r = 0
    for line in lines:
        x = []
        for i in range(len(line)):
            if line[i].isnumeric():
                x.append(line[i])
            elif part == 2:
                for abc, num in D.items():
                    if line[i:].startswith(abc):
                        x.append(num)
        if x:
            r += int(x[0] + x[-1])
    print(r)


f(1)
f(2)
