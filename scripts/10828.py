# Stack

N = int(input())

stack = []
for _ in range(N):
    op = input().split()  # operator, operand
    if op[0] == 'push':
        stack.append(op[1])
    elif op[0] == 'pop':
        try:
            print(stack.pop())
        except IndexError as e:
            print(-1)
    elif op[0] == 'size':
        print(len(stack))
    elif op[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif op[0] == 'top':
        if len(stack) != 0:
            print(stack[len(stack) - 1])
        else:
            print(-1)