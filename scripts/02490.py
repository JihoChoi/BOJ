# Yut

for i in range(3):
    # y1, y2, y3, y4 = map(int, input().split())
    yut = list(map(int, input().split()))  # u:0 n:1
    ys = sum(yut)
    if ys == 3:  # 1 1 1 0
        print('A')
    elif ys == 2:
        print('B')
    elif ys == 1:
        print('C')
    elif ys == 0:
        print('D')
    elif ys == 4:
        print('E')
