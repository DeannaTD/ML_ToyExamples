import re

def rtd(s):
    romans = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    for i in range(len(s)-1):
        if romans[s[i]] < romans[s[i+1]]:
            result -= romans[s[i]]
        else:
            result += romans[s[i]]
    result = result + romans[s[-1]]
    return result

s = input()

r = re.findall(r'[I|V|X|L|C|D|M]+', s)

for rn in r:
    s = s.replace(rn, str(rtd(rn)))
print(s)
