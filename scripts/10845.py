# Queue
# cf. Stack #10828

queue = []
for _ in range(int(input())):
    op = input().split()  # operator, operand
    if op[0] == 'push':
        queue.append(op[1])
    elif op[0] == 'pop':
        try:
            print(queue.pop(0))
        except IndexError as e:
            print(-1)
    elif op[0] == 'size':
        print(len(queue))
    elif op[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif op[0] == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif op[0] == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)
