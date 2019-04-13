# nCk

N, K = map(int, input().split(' '))

# denominator
denominator = 1
for i in range(0, K):
    denominator *= N
    N -= 1

# numerator
numerator = 1
for i in range(K, 0, -1):
    numerator *= i

print(denominator // numerator)