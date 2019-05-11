# DP
# Reference: https://hongku.tistory.com/266

import sys

N = int(sys.stdin.readline())

costs = []
dp = [[0]*3 for _ in range(N)]

for _ in range(N):
    costs.append(list(map(int, sys.stdin.readline().split())))

for i in range(0, N):
    dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])  # R
    dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])  # G
    dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])  # B

print(min(dp[i]))
