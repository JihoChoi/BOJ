stack = []
isVPS = True  # Valid Parenthesis String
ans = 0

for v in list(input()):

    if v == '(' or v == '[':
        stack.append(v)

    else:
        # v == ')' or ']'

        if len(stack) == 0 or not isVPS:
            isVPS = False
            break

        if stack[-1] == '(' and v == ')':
            stack.pop()
            stack.append(2)

        elif stack[-1] == '[' and v == ']':
            stack.pop()
            stack.append(3)

        else:
            value = 0
            # Top value is number
            while True:

                if len(stack) == 0 or not isVPS:
                    isVPS = False
                    break

                top = stack.pop()
                if isinstance(top, int):
                    value += top
                else:
                    if top == '(' and v == ')':
                        value *= 2
                        break
                    elif top == '[' and v == ']':
                        value *= 3
                        break
                    else:
                        isVPS = False
                        break

            stack.append(value)

if not isVPS:
    print(0)
else:
    try:
        print(sum(stack))
    except:
        print(0)
