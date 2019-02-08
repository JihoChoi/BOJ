# Sequence of Differences (계차 수열)
#     02 -> 08 -> 20 -> 38 ->
#       +06   +12   +18   +24

n = int(input())

sum = 2
count = 0
while not (n <= sum-1):
    count += 1
    sum += 6*count

print(count + 1)