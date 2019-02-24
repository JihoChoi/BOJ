# TAGs: REVIEW

# Number Theory
# Goldbach’s Conjecture

# Sieve of Eratosthenes (에라토스테네스의 체)


def prime_list(max_num):
    primes = list(range(max_num + 1))
    primes[1] = 0

    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = 0
    return primes


prime_list = prime_list(10000)

T = int(input())

for _ in range(T):
    n = int(input())

    i = n // 2
    j = n // 2

    while i > 0:
        if prime_list[i] != 0 and prime_list[j] != 0:
            print(i, j)
            break
        else:
            i -= 1
            j += 1
