# The Little Prince

# References
#       https://m.blog.naver.com/occidere/221048019075
#       https://jeonggyun.tistory.com/7

"""
Possible Cases
    1) (x1,y1) (x2,y2) both are in the inside of the circle
    2) (x1,y1) (x2,y2) both are at the outside of the circle
    3) (x1,y1) (x2,y2) only one of it is in the circle
"""

import sys
import math

T = int(input())

for _ in range(T):

    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())

    count = 0

    for _ in range(n):
        cx, cy, r = map(int, input().split())

        # distance from center of circle to the point
        dist_a = math.sqrt((cx - x1)**2 + (cy - y1)**2)
        dist_b = math.sqrt((cx - x2)**2 + (cy - y2)**2)

        flag_a_inside = False
        flag_b_inside = False

        if dist_a < r:
            flag_a_inside = True

        if dist_b < r:
            flag_b_inside = True

        if flag_a_inside != flag_b_inside:
            count += 1

    print(count)