# Chebyshev's Theorem
# Sieve of Eratosthenes (에라토스테네스의 체)

inputs = []
while True:
    n = int(input())
    if n == 0:
        break
    inputs.append(n)

primes = list(range(1, 2*max(inputs) + 1)) # sieve
primes.insert(0, 0)

for i in range(2, int(primes[-1] ** 0.5) + 1):
    if primes[i] != False:
        for j in range(i+i, len(primes), i):
            primes[j] = False

# print(primes)

for n in inputs:
    count = 0
    for i in range(n+1, 2*n+1):

        if primes[i] != False:
            count += 1
        # print(i)
    print(count)

"""
import math
from bisect import bisect

primes = list(range(123456 * 2 + 1))
primes[1] = 0
for i in range(2, int(math.sqrt(123456 * 2)) + 1):
    if primes[i]:
        for j in range(i * i, 123456 * 2 + 1, i):
            primes[j] = 0

primes = list(filter(None, primes))

N = int(input())
while (N != 0):
    print(bisect(primes, N * 2) - bisect(primes, N))
    N = int(input())
"""


