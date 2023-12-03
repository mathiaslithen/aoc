#!/usr/bin/python
import argparse
import datetime
import os
import subprocess


def main():
    n = datetime.datetime.now()
    p = argparse.ArgumentParser(description='Get AOC input')
    p.add_argument('-y', '--year', type=int, default=n.year)
    p.add_argument('-d', '--day', type=int, default=n.day)
    p.add_argument('dy', type=int, nargs='*')
    a = p.parse_args()
    d = a.day
    y = a.year
    if a.dy:
        d = a.dy[0]
        if len(a.dy) == 2:
            y = a.dy[1]
    u = 'https://adventofcode.com/%d/day/%d/input' % (y, d)
    c = '--cookie "session=%s"' % os.getenv('AOC_SESSION')
    x = subprocess.check_output(f'curl {u} {c}', shell=True)
    with open('%d.in' % d, 'wb') as f:
        f.write(x)


if __name__ == '__main__':
    main()
