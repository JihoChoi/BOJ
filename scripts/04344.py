# Rounding

N = int(input())

for i in range(N):
    scores = list(map(int, input().split()))
    avg = sum(scores[1:]) / scores[0]
    count = 0
    for score in scores[1:]:
        if score > avg:
            count += 1
    print("%.3f%%" % round(count / scores[0] * 100, 3))