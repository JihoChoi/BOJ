a, b = map(str, input().split())

a_2, a_1, a_0 = int(a[0]), int(a[1]), int(a[2])
b_2, b_1, b_0 = int(b[0]), int(b[1]), int(b[2])

a = a_0 * 100 + a_1 * 10 + a_2 * 1
b = b_0 * 100 + b_1 * 10 + b_2 * 1

if a > b:
    print(a)
else:
    print(b)
