# LCM: Least Common Multiple

import sys

def lcm(a, b):
    if a > b:
        a, b = b, a
    ans = a
    while ans % b != 0:
        ans += a
    return ans

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a, b))

"""

def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

def lcm(a, b):
    return (a * b) / gcd(a, b)
"""
