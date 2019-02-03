# Self Number

self_num_set = set(i for i in range(1,10001))
generated_num_set = set()

for i in range(1, 10001):
    generated_num_set.add(i + sum(map(int, str(i))))

self_num_set -= generated_num_set

for i in sorted(self_num_set):
    print(i)