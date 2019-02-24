# Prime Numbers, Sieve of Eratosthenes

N = int(input())
nums = list(map(int, input().split(' ')))
count = 0

for n in nums:
    if n == 1:
        continue
    isPrime = True
    for i in range(2, n):
        if n % i == 0:
            isPrime = False
            break
    if isPrime:
        count += 1

print(count)


# Sieve of Eratosthenes (에라토스테네스의 체)
"""
def prime_list(max_num):
    sieve = [True] * (max_num + 1) # Sieve of Eratosthenes
    m = int(max_num ** 0.5) # sqrt(n)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, max_num+1, i):
                sieve[j] = False
    return [i for i in range(2, max_num+1) if sieve[i] == True]

N = int(input())
nums = list(map(int, input().split(' ')))
count = 0
primes = prime_list(max(nums))

for i in range(N):
    if nums[i] in primes :
        count += 1

print(count)
"""