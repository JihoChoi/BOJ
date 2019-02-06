n = int(input())
sum = 0
k = 0

while sum < n:
    k += 1
    sum += k

sum -= k
count = n - sum

if k % 2 == 0:
    print("{1}/{0}".format(k - count + 1, count))
else:
    print("{0}/{1}".format(k - count + 1, count))