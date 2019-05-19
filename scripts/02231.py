import sys

# 198 -> 216
# 198 + 1 + 9 + 8 = 216

N = int(sys.stdin.readline())

HAS_CONSTRUCTOR = False

for i in range(N):
    if sum(map(int, str(i))) + i == N:
        HAS_CONSTRUCTOR = True
        print(i)
        break

if not HAS_CONSTRUCTOR:
    print(0)
