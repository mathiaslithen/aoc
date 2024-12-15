import re


def _rc(G):
    return len(G), len(G[0])


def INTS(line):
    x = re.findall(r'\-?\d+', line)
    if x:
        return list(map(int, x))


def INB(G, rr, cc):
    R, C = _rc(G)
    return 0 <= rr < R and 0 <= cc < C


def RC(G):
    R, C = _rc(G)
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


def GFIND(G, x):
    ret = []
    for r, c in RC(G):
        v = G[r][c]
        if callable(x):
            valid = x(v)
        else:
            valid = x == v
        if valid:
            ret.append((r, c))
    return ret

def VIS(G):
    print('\n'.join(''.join(str(i) for i in line) for line in G), '\n')

def DIM(G):
    return len(G), len(G[0])
