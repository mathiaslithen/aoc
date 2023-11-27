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
    a = p.parse_args()
    u = 'https://adventofcode.com/%d/day/%d/input' % (a.year, a.day)
    c = '--cookie "session=%s"' % os.getenv('AOC_SESSION')
    x = subprocess.check_output(f'curl {u} {c}', shell=True)
    with open('%d.in' % a.day, 'wb') as f:
        f.write(x)


if __name__ == '__main__':
    main()
