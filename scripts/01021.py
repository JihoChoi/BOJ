import sys

# REVIEW

# References
# https://parkssiss.tistory.com/42
# https://roseline124.github.io/algorithm/2019/04/06/Altorithm-baekjoon-1021.html

N, M = map(int, sys.stdin.readline().split(' '))
pos = list(map(int, input().split(' ')))  # positions, locations

count = 0  # step count
deque = list(range(1, N+1))

"""
def shift_left(deque):  # (2) front to back
    global count
    count += 1
    deque.append(deque.pop(0))

def shift_right(deque):  # (3) back to front
    global count
    count += 1
    # deque = [deque.pop(-1)] + deque  # requires return
    deque.insert(0, deque.pop(-1))
"""

while pos:
    if pos[0] == deque[0]:
        pos.pop(0)
        deque.pop(0)
    else:
        if deque.index(pos[0]) <= len(deque) // 2:
            while deque[0] != pos[0]:
                # shift_left(deque)
                deque.append(deque.pop(0))
                count += 1
        else:
            while deque[0] != pos[0]:
                # shift_right(deque)
                deque.insert(0, deque.pop(-1))
                count += 1
print(count)