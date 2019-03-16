# Josephus Problem
# References 01158, 11866

N, M = map(int, input().split())

queue = list(range(1, N+1))
result = []

count = 0
while queue:
    count += 1
    if count == M:
        result.append(queue.pop(0))
        count = 0
    else:
        queue.append(queue.pop(0))  # move to tail

output = ''
for n in result:
    output += str(n) + ', '
print('<' + output[:-2] + '>')
