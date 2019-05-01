# nCk

n, m = map(int, input().split(' '))

# numerator
numerator = 1
for i in range(0, m):
    numerator *= n
    n -= 1

# denominator
denominator = 1
for i in range(m, 0, -1):
    denominator *= i

print(numerator // denominator)