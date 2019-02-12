"""
N = int(input())

nums = []
for _ in range(N):
    nums.append(int(input()))

nums.sort()
for num in nums:
    print(num)
"""

import sys
N = int(input())
nums = [0] * 10001

for i in range(N):
    a = int(sys.stdin.readline())
    nums[a] = nums[a] + 1

for i in range(len(nums)):
    if nums[i] !=0:
        for count in range(nums[i]):
            print(i)