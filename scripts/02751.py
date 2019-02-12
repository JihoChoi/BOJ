"""
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort()
for num in nums:
    print(num)
"""


# Using Index: Without Sorting

import sys

N = int(input())
nums = [0] * 2000003

for i in range(N):
    index = int(sys.stdin.readline())
    # No Duplicates
    if index >= 0:
        nums[index] = 1
    else:
        nums[index * (-1) + 1000000] = 1

for i in reversed(range(1000001, 2000003)):
    """
    try:
        if nums[i] == 1:
            print( (i - 1000000) * (-1) )
    except Exception as e:
        print(i)
        raise e
    """
    if nums[i] == 1:
        print( (i - 1000000) * (-1) )

for i in range(1000001):
    if nums[i] == 1:
        print(i)