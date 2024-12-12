import re


def INTS(line):
    x = re.findall(r'\d+', line)
    if x:
        return list(map(int, x))


def INB(R, C, rr, cc):
    return 0 <= rr < R and 0 <= cc < C


def RC(R, C):
    yield from [(r, c) for r in range(R) for c in range(C)]


def DRC():
    DR = [0, 0, 1, -1]
    DC = [1, -1, 0, 0]
    yield from zip(DR, DC)


def DIAG():
    DR = [-1, 1, -1, 1]
    DC = [1, -1, -1, 1]
    yield from zip(DR, DC)


def ALLD():
    yield from (*DRC(), *DIAG())


def GFIND(G, R, C, x):
    ret = []
    for r, c in RC(R, C):
        v = G[r][c]
        if callable(x):
            valid = x(v)
        else:
            valid = x == v
        if valid:
            ret.append((r, c))
    return ret
