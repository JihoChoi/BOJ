# TODO: Recursive

def sum(k, n):
    arr = [i for i in range(1, n+1)]
    for _ in range(k):
        for j in range(1, n):
            arr[j] += arr[j-1]
    return arr[-1]

T = int(input())

for _ in range(T):
    k = int(input()) # 1
    n = int(input()) # 3
    print(sum(k, n))