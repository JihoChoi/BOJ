# Dynamic Programming (동적 계획법)
#   DP, memoization, fibonacci

# References
# https://pyformat.info/
# https://github.com/soakdma37/BOJ

import sys

T = int(input())
MAX = 40

# dp, memo, cache, ...
# dp = [{'zero': 0, 'one': 0}] * (MAX + 1)

# List in Python is not array, linked list (pointer array)
dp = []
dp.append({'zero': 1, 'one': 0}) # dp[0]
dp.append({'zero': 0, 'one': 1}) # dp[1]

for i in range(2, MAX + 1):
    dic = {}
    dic['zero'] = dp[i-2]['zero'] + dp[i-1]['zero']
    dic['one'] = dp[i-2]['one'] + dp[i-1]['one']

    dp.append(dic) # dp[i]
    # print('{:02d} {} {}'.format(i, dp[i]['zero'], dp[i]['one']))

for _ in range(T):
    i = int(input())
    print('{} {}'.format(dp[i]['zero'], dp[i]['one']))