# DP

import sys

N = int(sys.stdin.readline())

nums = []
dp = [[0]*N for _ in range(N)]


for _ in range(N):
    nums.append(list(map(int, sys.stdin.readline().split())))

for i in range(0, N):
    for j in range(i+1):
        dp[i][j] = nums[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[i]))
