import sys
from collections import defaultdict


sys.setrecursionlimit(30000)

def xin():
    _in = input()
    while _in.strip() == "":
        _in = input()
    return _in

def getints():
    return [int(x) for x in xin().strip().split()]

def getint():
    return int(xin())

def num(s):
    x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a = 0
    for d in x:
        if d in s:
            a += 1
    return a

for case in range(1, 1+getint()):
    n = getint()
    winner = None
    for i in range(n):
        name = input()
        if winner == None:
            winner = name
        else:
            nw = num(winner)
            nn = num(name)
            if nw < nn or (nw == nn and name < winner):
                winner = name

    print("Case #{}: {}".format(case, winner))
