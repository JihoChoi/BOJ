A = int(input())
B = int(input())
C = int(input())

num = A*B*C
for i in range(0, 10):
    print(str(num).count(str(i)))