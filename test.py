s = input()
r = ""
for i in range(len(s)):
    if(s[i] == 'a'):
        r += 'b'
    elif(s[i] == 'b'):
        r += 'a'
    elif(s[i] == 'A'):
        r += 'B'
    elif(s[i] == 'B'):
        r += 'A'
    else:
        r += s[i]

print(r)
