N = int(input())

for _ in range(N):
    input_str = str(input())
    flag = 0
    score = 0
    for i in range(0, len(input_str)):
        if input_str[i] == 'O':
            flag += 1
            score += flag
        else:
            flag = 0
    print(score)