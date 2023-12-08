#!/usr/bin/python
import math
import sys

fn = sys.argv[1] if len(sys.argv) > 1 else '8.in'
with open(fn) as f:
    data = f.read().strip()
lines = data.split('\n\n')

inst = [0 if c == 'L' else 1 for c in lines[0]]
G = {}
for line in lines[1].split('\n'):
    w = line.split()
    G[w[0]] = [w[2].strip(',()'), w[3].strip(',()')]

current = 'AAA'
finish = 'ZZZ'
i = 0
L = len(inst)
A = 0
while True:
    if current == finish:
        break
    A += 1
    instruction_index = i % L
    j = inst[instruction_index]
    current = G[current][j]
    i += 1
print(A)

nodes = []
for n in G:
    if n[-1] == 'A':
        nodes.append(n)
B = 0
D = []
i = 0
while nodes:
    for n in nodes:
        if n[-1] == 'Z':
            D.append(B)
    nodes = [n for n in nodes if n[-1] != 'Z']
    B += 1
    instruction_index = i % L
    j = inst[instruction_index]
    new_nodes = []
    for n in nodes:
        new_nodes.append(G[n][j])
    i += 1
    nodes = new_nodes
print(math.lcm(*D))
