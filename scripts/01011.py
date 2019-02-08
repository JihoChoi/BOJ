T = int(input())

for _ in range(T):
    x, y = map(int, input().split())

    total_move = 0
    count = 0

    while total_move < y - x:
        count += 1
        total_move += count // 2
    
    print(count-1)


# print(int(2 * (dist - 0.5) ** 0.5))