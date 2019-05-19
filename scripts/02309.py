import sys

def find_index(heights):
    height_sum = sum(heights)
    for i in range(9):
        for j in range(i+1, 9):
            if height_sum - heights[i] - heights[j] == 100:
                return heights[i], heights[j]

heights = [int(sys.stdin.readline()) for _ in range(9)]
heights.sort()

n1, n2 = find_index(heights)

for height in heights:
    if height != n1 and height != n2:
        print(height)
