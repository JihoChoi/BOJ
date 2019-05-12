# GCD: Greatest Common Divisor

import sys

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

N = int(sys.stdin.readline())

radius = list(map(int, sys.stdin.readline().split()))

R = radius[0]
for r in radius[1:]:
    # print(R, r)
    g = gcd(R, r)
    print("{0}/{1}".format(R//g, r//g))
