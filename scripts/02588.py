num1 = int(input())
num2 = int(input())

for n in reversed(list(str(num2))):
    print(num1 * int(n))

print(num1 * num2)


