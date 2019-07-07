n1, n2 = map(int, input().split())

if n2 >= 45:
    print(n1, n2 - 45)
else:
    if n1 > 0:
        print(n1 - 1, n2 + 60 - 45)
    elif n1 == 0:
        print(23, n2 + 60 - 45)
