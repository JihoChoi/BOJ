# DP - iterations

# Review
# Reference - http://leechoong.com/posts/2018/boj_1463/

import sys

N = int(sys.stdin.readline())
dp = [0, 0, 1, 1]  # 0, 1, 2, 3

# dp[i] = min([dp[i-1], dp[i//2], dp[i//3]]) + 1
for i in range(4, N + 1):
    dp.append(dp[i-1] + 1)

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])
