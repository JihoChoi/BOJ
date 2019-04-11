

# REVIEW
# https://onsil-thegreenhouse.github.io/programming/problem/2018/03/29/problem_fibo/
# https://egg-money.tistory.com/78

n = int(input())

fib = [0, 1]

mod = 1000000
r = mod // 10*15  # range

for i in range(2, r):
    fib.append(fib[i-1] + fib[i-2])
    fib[i] = fib[i] % mod

print(fib[n % r])