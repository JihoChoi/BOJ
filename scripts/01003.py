# Dynamic Programming (동적 계획법)
#   DP, memoization, fibonacci


# References
# https://pyformat.info/
# https://github.com/soakdma37/BOJ


import sys

T = int(input())
MAX = 40

# dp, memo, cache, ...
dp = [{'zero': 0, 'one': 0}] * (MAX + 1)
dp[0] = {'zero': 1, 'one': 0}
dp[1] = {'zero': 0, 'one': 1}

# print('{} {}'.format(dp[0]['zero'], dp[0]['one']))
# print('{} {}'.format(dp[1]['zero'], dp[1]['one']))
# print(dp)

# for i in range(2, MAX + 1):
for i in range(2, 4):
    dp[i]['zero'] = dp[i-2]['zero'] + dp[i-1]['zero']
    dp[i]['one'] = dp[i-2]['one'] + dp[i-1]['one']

    print(dp[i]['one'], dp[i-2]['one'], dp[i-1]['one'])
    print(dp[i-2]['zero'], "+", dp[i-1]['zero'])
    print(dp[i-2]['one'], "+", dp[i-1]['one'])
    print('{:02d} {} {}'.format(i, dp[i]['zero'], dp[i]['one']))


# for _ in range(T):
#     print('{} {}'.format(dp[i]['zero'], dp[i]['one']))
