N, X = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(N):
    if X > nums[i]:
        print(nums[i], end=' ')