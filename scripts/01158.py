# Josephus Problem, Indexing
# References 01158, 11866

N, M = map(int, input().split())

queue = list(range(1, N+1))
result = []

index, count, pop_count = 0, 0, 0

while queue:

    index = (index + M - 1) % len(queue)
    result.append(queue.pop(index))


output = ''
for n in result:
    output += str(n) + ', '
print('<' + output[:-2] + '>')
