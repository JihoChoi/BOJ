import math

fac = math.factorial(int(input()))
count = 0

while fac % 10 == 0:
    count += 1
    fac //= 10

print(count)
