# Stack, Parenthesis

T = int(input())
for _ in range(T):
    paren_string = list(input())
    # print(paren_string)
    stack = []
    isValid = True
    for i, val in enumerate(paren_string):
        if paren_string[i] == '(':
            stack.append(paren_string[i])
        else:
            if len(stack) == 0:
                isValid = False
                break
            if stack[-1] == '(':
                stack.pop()
            else:
                isValid = False
                break
    if len(stack) == 0 and isValid:
        print("YES")
    else:
        print("NO")


# Reference: https://ksw626.tistory.com/96
'''
for i in range(int(input())):
    vps = list(input())
    while len(vps) != 0:
        if vps[0] == ')' or vps[-1] == '(':
            print('NO')
            break
        else:
            if '(' and ')' in vps:
                vps.remove('(')
                vps.remove(')')
            else:
                print('NO')
                break
    if len(vps) == 0:
        print('YES')
'''