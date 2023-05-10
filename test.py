import re

s = input()

r = re.findall(r'[cC][eEiIyY]', s)

for i in r:
    s = s.replace(i, 's' + i[1])

s = s.replace('c', 'k').replace('C', 'K')
s = s.replace('Qu', 'Kv').replace('qu', 'kv')
s = s.replace('q', 'k').replace('Q', 'K')
s = s.replace('x', 'ks').replace('X', 'Ks')
s = s.replace('w', 'v').replace('W', 'V')
s = s.replace('Ph', 'F').replace('ph', 'f')
s = s.replace('You', 'u').replace('you', 'u')
s = s.replace('Oo', 'u').replace('oo', 'u')
s = s.replace('Ee', 'i').replace('ee', 'i')
s = s.replace('Th', 'Z').replace('th', 'z')

r = re.finditer(r'([bcdfghjklmnpqrstvwxz])\1', s)
n = next(r, False)
while n:
    s = s.replace(n.group(), n.group()[0])
    n = next(r, False)
print(s)
