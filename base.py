#!/usr/bin/python
import sys

fn = sys.argv[1] if len(sys.argv) > 1 else 'n.in'
with open(fn) as f:
    data = f.read().strip()
lines = data.split('\n')
