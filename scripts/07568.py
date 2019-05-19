import sys

N = int(sys.stdin.readline())

input_list = []
for _ in range(N):
    x, y = sys.stdin.readline().strip().split(" ")
    input_list.append((x, y))

ranks = [1] * N
for i in range(N):
    for j in range(i+1, N):
        x, y = input_list[i]
        p, q = input_list[j]

        if x < p and y < q:
            ranks[i] += 1
        elif x > p and y > q:
            ranks[j] += 1

print(" ".join(str(rank) for rank in ranks))