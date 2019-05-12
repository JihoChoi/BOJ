# LCM: Least Common Multiple

import sys

def lcm(a, b):
    if a > b:
        a, b = b, a
    ans = a
    while ans % b != 0:
        ans += a
    return ans

a, b = map(int, sys.stdin.readline().split())
print(lcm(a, b))
