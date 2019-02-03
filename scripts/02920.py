nums = list(map(int, input().split(" ")))

if nums == sorted(nums): # if nums == sorted(nums, reverse=False):
    print("ascending")
elif nums == sorted(nums, reverse=True):
    print("descending")
else:
    print("mixed")