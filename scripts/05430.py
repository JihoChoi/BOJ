"""
import sys

for _ in range(int(sys.stdin.readline())):

    functions = list(sys.stdin.readline())  # functions
    n = int(sys.stdin.readline())
    # nums = list(map(int, input()[1:-1].split(',')))  # 1:-1 for slicing
    # nums = list(sys.stdin.readline()[1:-1].split(','))
    nums = eval(sys.stdin.readline())

    error_flag = False
    for func in functions:
        # print('nums:', nums)
        if func == 'R':
            # nums = nums[::-1]
            nums.reverse()
        elif func == 'D':
            try:
                nums.pop(0)
            except:
                sys.stdout.write('error\n')
                error_flag = True
                break

    if not error_flag:
        print(nums)
"""


import sys

def error_msg():
    global e
    print("error")
    e = True

T = int(sys.stdin.readline())

for _ in range(T):
    e = False
    cmds = list(sys.stdin.readline().strip())
    n = int(sys.stdin.readline())
    nums = list(sys.stdin.readline().strip()[1:-1].split(','))

    if nums[0] == "":
        nums.pop()

    r = False
    for x in cmds:
        if x == "R":
            r = not r
        elif x == "D":
            if not nums:
                error_msg()
                break;
            nums.pop(r*(-1))

    if not e:
        print("[" + ','.join(reversed(nums) if r else nums) + "]")

