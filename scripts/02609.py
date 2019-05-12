# LCM: Least Common Multiple
# GCD: Greatest Common Divisor

import sys

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcd(a, b):
    if a > b:
        a, b = b, a
    ans = a
    while ans % b != 0:
        ans += a
    return ans

a, b = map(int, sys.stdin.readline().split())
print(gcd(a, b))
print(lcd(a, b))