# Group Words

from string import ascii_lowercase

N = int(input())

count = 0
for _ in range(N):

    prev_char = None
    alphabet = {}
    for c in ascii_lowercase:
        alphabet[c] = False

    word = input()

    length = 0
    for i in word:
        if alphabet[i] == True and prev_char != i:
            break;
        alphabet[i] = True
        prev_char = i
        length += 1
        if length == len(word):
            count += 1

print(count)