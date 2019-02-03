s = input()

while len(s) > 10:
    print(s[0:10], end='\n')
    s = s[10:]

if len(s) != 0:
    print(s)


# Reference: https://cleancode-ws.tistory.com/60
"""
s = input()
for i in range(0, len(s), 10):
    print(s[i: i+10])
"""