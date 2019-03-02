# Deque
# cf. Stack #10828, deque #10845

deque = []
for _ in range(int(input())):
    op = input().split()  # operator, operand
    if op[0] == 'push_front':
        deque.insert(0, op[1])
    elif op[0] == 'push_back':
        deque.append(op[1])
    elif op[0] == 'pop_front':
        try:
            print(deque.pop(0))
        except IndexError as e:
            print(-1)
    elif op[0] == 'pop_back':
        try:
            print(deque.pop())
        except IndexError as e:
            print(-1)
    elif op[0] == 'size':
        print(len(deque))
    elif op[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif op[0] == 'front':
        if len(deque) != 0:
            print(deque[0])
        else:
            print(-1)
    elif op[0] == 'back':
        if len(deque) != 0:
            print(deque[-1])
        else:
            print(-1)
