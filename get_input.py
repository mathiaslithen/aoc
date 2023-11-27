#!/usr/bin/python
import argparse
import datetime
import os
import subprocess

S = None


def main():
    p = argparse.ArgumentParser(description='Get AOC input')
    n = datetime.datetime.now()
    p.add_argument('-y', '--year', type=int, default=n.year)
    p.add_argument('-d', '--day', type=int, default=n.day)
    a = p.parse_args()
    s = S or os.getenv('AOC_SESSION')
    u = 'https://adventofcode.com/%d/day/%d/input' % (a.year, a.day)
    c = ' '.join(['curl', u, '--cookie "session=%s"' % s])
    x = subprocess.check_output(c, shell=True)
    with open('%d.in' % a.day, 'wb') as f:
        f.write(x)


if __name__ == '__main__':
    main()
