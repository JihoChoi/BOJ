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

M, N = map(int, input().split(" "))
primes = prime_list(M, N)

for prime in primes:
    print(prime)