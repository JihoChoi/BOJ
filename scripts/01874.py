# Stack

N = int(input())

num_stack = []
ans_list = []
count = 1
isPossible = True

for _ in range(N):
    num = int(input())
    while count <= num:
        num_stack.append(count)
        ans_list.append('+')
        count += 1

    if num_stack[-1] == num:
        num_stack.pop()
        ans_list.append('-')
    else:
        print("NO")
        isPossible = False
        break

# if len(num_stack) == 0:
if isPossible:
    for s in ans_list:
        print(s)