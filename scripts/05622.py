# 65 66 67 -> 2
# 68 69 70 -> 3 ...

s = input()
d = ['ACB','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time = 0
for c in s:
    for i in d:
        if c in i:
            time += d.index(i) + 3
print(time)

# Reference: https://sssunho.tistory.com/50
# print(sum(min(ord(c)-64,25)*28//89+3for c in input()))