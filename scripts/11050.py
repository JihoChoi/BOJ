# nCk

N, K = map(int, input().split(' '))

# numerator
numerator = 1
for i in range(0, K):
    numerator *= N
    N -= 1

# denominator
denominator = 1
for i in range(K, 0, -1):
    denominator *= i

print(numerator // denominator)