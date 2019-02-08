# GCD, LCM
"""
T = int(input())

def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm

for _ in range(T):
    M, N, x, y = map(int(), input().split())

"""

def get_year(m, n, x, y):
    while x <= m * n:
        if (x-y) % n == 0:
            return x
        x += m
    return -1

T = int(input())
for _ in range(T):
    m, n, x, y = map(int, input().split())
    print(get_year(m,n,x,y))