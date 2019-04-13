# nCk

n, k = map(int, input().split(' '))

while n != 0 or k != 0:

    if k > n // 2:
        k = n - k
    # denominator
    denominator = 1
    for i in range(0, k):
        denominator *= n
        n -= 1

    # numerator
    numerator = 1
    for i in range(k, 0, -1):
        numerator *= i

    print(denominator // numerator)

    n, k = map(int, input().split(' '))
