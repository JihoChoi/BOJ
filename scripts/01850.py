# GCD: Greatest Common Divisor
# REVIEW Euclidean Algorithm

import sys

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a, b = map(int, sys.stdin.readline().split())
ans = ['1'] * gcd(a, b)

print("".join(ans))

