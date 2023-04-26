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

r = re.finditer(r'[I|V|X|L|C|D|M]+', s)
n = next(r, False)

while(n):
    start = n.span()[0]
    end = n.span()[1]
    s = s[:start] + str(rtd(s[start:end])) + s[end:]
    r = re.finditer(r'[I|V|X|L|C|D|M]+', s)
    n = next(r, False)

print(s)
