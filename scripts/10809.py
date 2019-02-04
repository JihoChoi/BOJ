from string import ascii_lowercase

s = input()

for c in ascii_lowercase:
    print(s.find(c), end=' ')