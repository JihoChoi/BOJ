from math import log
#  N = 3×2^k, k = 0, 1, 2, ..., 10

N = int(input())
k = int(log(N // 3, 2))

stars = ['  *   ',' * *  ','***** ']

def append_stars(size):
    for i in range(len(stars)):
        stars.append(stars[i] + stars[i])
        stars[i] = ' '*size + stars[i] + ' '*size
        # print(stars[i], i)

for i in range(k):
    # print(i)
    append_stars(3*2**i)

# Print
for i in range(len(stars)):
    print(stars[i])