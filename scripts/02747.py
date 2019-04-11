n = int(input())
fib = [0, 1]

count = 0
while count < n:
    fib.append(fib[count] + fib[count+1])
    count += 1

print(fib[count])

'''
x = [0, 1]
for i in range(1, int(input())):
    x += [x[i] + x[i-1]]
print(x[-1])
'''