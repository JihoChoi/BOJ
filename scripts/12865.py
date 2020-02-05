
"""
TAG: 0-1 Knapsack Problem, Dynamic Programming (DP), O(nW)

References:
    - https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

weights and values of n items, capacity -> max value

"""

N, W = map(int, input().split())  # number of items, capacity

weights = []
values = []
for i in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)


def knapsack(W, weights, values, n):
    dp = [[0 for x in range(W+1)] for x in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][W]


print(knapsack(W, weights, values, N))


# Naive
"""
def knapsack(W, weights, values, n):
    if n == 0 or W == 0:  # base
        return 0

    if (weights[n-1] > W):
        return knapsack(W, weights, values, n-1)
    else:
        return max(
            values[n-1] + knapsack(W - weights[n-1], weights, values, n-1),
            knapsack(W, weights, values, n-1)
        )
"""
