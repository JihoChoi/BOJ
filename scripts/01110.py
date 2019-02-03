N = int(input())
a, b = divmod(N, 10)

count = 0
while True:
    c, d = divmod(a + b, 10)
    a, b = b, d
    count += 1
    # print(a, b, c, d)
    if a*10+b == N:
        break;
print(count)