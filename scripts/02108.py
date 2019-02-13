# Mean, Median, Mode, Range

import sys
from collections import Counter

N = int(sys.stdin.readline())
nums = []

for i in range(N):
    nums.append(int(sys.stdin.readline()))

print(round(sum(nums) / len(nums)))

sort_nums = sorted(nums) # nums.sort()
print(sort_nums[len(sort_nums) // 2])

count = Counter(sort_nums)
count = sorted(count.items(), key=lambda x: (-x[1], x[0])) # sort by count & sort by value
if len(count) != 1 and count[0][1] == count[1][1]:
    print(count[1][0])
else:
    print(count[0][0])

print(sort_nums[-1] - sort_nums[0])