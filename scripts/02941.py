s = input()
a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for c in a:
    s = s.replace(c, '~')
print(len(s))