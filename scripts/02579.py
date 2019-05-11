# DP stairs

import sys

N = int(sys.stdin.readline())
nums = []
dp = [0] * N

for _ in range(N):
    nums.append(int(sys.stdin.readline()))

dp[0] = nums[0]
dp[1] = nums[1] + dp[0]
dp[2] = nums[2] + max(nums[0], nums[1])

for i in range(3, N):
    dp[i] = nums[i] + max(nums[i-1] + dp[i-3], dp[i-2])

print(dp[N-1])


'''
-----------------------------------------
0    1    2    3    4    5    6
    10   20   15   25   10   20

'''
