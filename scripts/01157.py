from string import ascii_uppercase
import operator

alphabet = {}
for c in ascii_uppercase:
    alphabet[c] = 0

S = input().upper()
for c in S:
    alphabet[c] += 1

sorted_alpha = sorted(alphabet.items(), key=operator.itemgetter(1), reverse=True) # Sort by value

if sorted_alpha[0][1] == sorted_alpha[1][1]:
    print("?")
else:
    print(sorted_alpha[0][0])