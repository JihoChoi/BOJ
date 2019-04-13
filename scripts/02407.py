# nCk

n, m = map(int, input().split(' '))

# denominator
denominator = 1
for i in range(0, m):
    denominator *= n
    n -= 1

# numerator
numerator = 1
for i in range(m, 0, -1):
    numerator *= i

print(denominator // numerator)