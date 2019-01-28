import math
import sys

n = int(input())

for _ in range(n):
    # x1, y1, r1, x2, y2, r2 = map(int, input().split())
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    if (x1 == x2 and y1 == y2 and r1 == r2):
        print("-1")
        continue

    r = r1
    R = r2

    if r1 > r2:
        r = r2
        R = r1

    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    if r + R < dist:
        print(0)
    elif r + R == dist:
        print(1)
    elif r + R > dist and dist > R - r:
        print(2)
    elif R - r == dist:
        print(1)
    elif R - r > dist:
        print(0)
