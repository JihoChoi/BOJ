# nCk

n, k = map(int, input().split(' '))

while n != 0 or k != 0:

    if k > n // 2:
        k = n - k
    # numerator
    numerator = 1
    for i in range(0, k):
        numerator *= n
        n -= 1

    # denominator
    denominator = 1
    for i in range(k, 0, -1):
        denominator *= i

    print(numerator // denominator)

    n, k = map(int, input().split(' '))
