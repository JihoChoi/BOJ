# Prime Numbers, Sieve of Eratosthenes

def prime_list(min_num, max_num):
    sieve = [True] * (max_num + 1) # Sieve of Eratosthenes
    m = int(max_num ** 0.5) # sqrt(n)

    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, max_num+1, i):
                sieve[j] = False

    sieve[1] = False
    return [i for i in range(min_num, max_num+1) if sieve[i] == True]

M = int(input())
N = int(input())

primes = prime_list(M, N)

if not primes:
    print("-1")
else:
    print(sum(primes))
    print(min(primes))